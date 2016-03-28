__author__   = "Justin Iravani"

import MySQLdb


raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()

raw_cursor.execute("""SELECT player_name_gen, team_gen FROM
                    (SELECT player_name_gen, team_gen FROM `mls_data_raw`.`locations`
                    UNION
                    SELECT player_name_1_gen, player_1_team_gen FROM `mls_data_raw`.events) a
                    GROUP BY player_name_gen
                    ORDER BY player_name_gen;""")

results = raw_cursor.fetchall()

for row in results:
    for item in row:
        sql = "INSERT INTO `mls_dw`.`dim_player`(`name`)VALUES(\"%s\");" % (item)

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
