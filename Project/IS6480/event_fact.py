__author__   = "Justin Iravani"

import MySQLdb

source = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
target = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

source_cursor = source.cursor()
target_cursor = target.cursor()
target_table = "event_fact"

target_cursor.execute("DELETE FROM %s WHERE 1=1;" % (target_table)) # empty table
target_cursor.execute("ALTER TABLE %s AUTO_INCREMENT = 1;" % (target_table)) # reset auto_increment


source_cursor.execute("""
SELECT p1_player_id, p2_player_id, t1_team_id, t2_team_id, a.date_id, period, time_from_zero, event_type_id, game_id  FROM
(
		SELECT 	h.team_id AS h_team_id, v.team_id AS v_team_id,
				IF(p1.player_id IS NULL,'null',p1.player_id) AS p1_player_id,
                IF(p2.player_id IS NULL,'null',p2.player_id) AS p2_player_id,
				IF(t1.team_id = 9999, 'null', t1.team_id) AS t1_team_id,
				IF(t2.team_id = 9999, 'null', t2.team_id) AS t2_team_id, d.date_id,
				IF(period_desc ='First Half',1,2) As period, time_from_zero, e.event_type_id

				FROM `mls_data_raw`.`events`

				LEFT JOIN mls_dw.dim_team           h       ON h_team_gen = h.name
				LEFT JOIN mls_dw.dim_team           v       ON v_team_gen = v.name
				LEFT JOIN mls_dw.dim_team   		t1 		ON player_1_team_gen = t1.name
				LEFT JOIN mls_dw.dim_team   		t2    	ON player_2_team_gen = t2.name
				LEFT JOIN mls_dw.dim_event_type  	e 		ON event_type = e.type
				LEFT JOIN mls_dw.dim_date        	d		ON date(game_date_gen) = d.date
				LEFT JOIN mls_dw.dim_player      	p1      ON player_name_1_gen = p1.name
				LEFT JOIN mls_dw.dim_player      	p2      ON player_name_2_gen = p2.name

				ORDER BY date_id, time_from_zero

)  a
		JOIN mls_dw.dim_game g 		ON 	g.home_id 		= h_team_id
									AND	g.visitor_id	= v_team_id
                                    AND g.date_id		= a.date_id;
""")

results = source_cursor.fetchall()
counter = 0
for row in results:
    counter += 1
    sql = """
        INSERT INTO `mls_dw`.`event_fact`
        (`prim_player_id`,`sec_player_id`,`prim_team_id`,`sec_team_id`,`date_id`,`period`,`time_from_zero`,`event_type_id`,`game_id`)
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s);""" % (row)

    print sql
    print counter
    try:
        # Execute the SQL command
        target_cursor.execute(sql)

        # Commit your changes in the database
        target.commit()

    except:
        # Rollback in case there is any error
        print "error"
        target.rollback()

source.close()
target.close()
