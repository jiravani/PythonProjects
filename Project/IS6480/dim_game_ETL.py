__author__   = "Justin Iravani"

import MySQLdb

raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()
target_table = "mls_dw.dim_game"

final_cursor.execute("DELETE FROM %s WHERE 1=1;" % (target_table))
final_cursor.execute("ALTER TABLE %s AUTO_INCREMENT = 1;" % (target_table))

raw_cursor.execute("""SELECT  h.team_id AS h_team_id,v.team_id AS v_team_id, date_id FROM
                                    (SELECT date(game_date_gen) AS date, v_team_gen, h_team_gen FROM mls_data_raw.locations
                                    UNION
                                    SELECT date(game_date_gen), v_team_gen, h_team_gen FROM mls_data_raw.events) a
                            	JOIN mls_dw.dim_team   v 		ON v_team_gen = v.name
                                JOIN mls_dw.dim_team   h     	ON h_team_gen = h.name
                                JOIN mls_dw.dim_date   d		ON a.date = d.date;""")

results = raw_cursor.fetchall()


for row in results:
    sql =   "INSERT INTO %s (`home_id`,`visitor_id`,`date_id`)" % (target_table) + \
            "VALUES (%d, %d, %d);" % (row)
#    print sql
    try:
        # Execute the SQL command
        final_cursor.execute(sql)
        # Commit your changes in the database
        final.commit()
    except:
        # Rollback in case there is any error
        print "error"
        final.rollback()
raw.close()
final.close()
