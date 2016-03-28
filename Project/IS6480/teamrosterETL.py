__author__   = "Justin Iravani"

import MySQLdb

raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()

raw_cursor.execute("""SELECT p.player_id, t.team_id, date(game_date_gen) FROM
                        (SELECT player_name_gen, team_gen, game_date_gen FROM `mls_data_raw`.`locations`
                        UNION
                        SELECT player_name_1_gen, player_1_team_gen, game_date_gen FROM `mls_data_raw`.events) a
                        JOIN mls_dw.dim_player p ON player_name_gen = p.name
                        JOIN mls_dw.dim_team t ON team_gen = t.name
                        WHERE team_gen not like "null"
                        group by player_id
                        ORDER BY t.team_id
                        ;""")

results = raw_cursor.fetchall()

for row in results:
    sql = "INSERT INTO `mls_dw`.`team_roster_fact`(`player_id`, `team_id`,`start_date`,`end_date`,`isActive`)" \
    "VALUES (%d, %d, \'%s\', null , 1);" % (row)
    print sql

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
