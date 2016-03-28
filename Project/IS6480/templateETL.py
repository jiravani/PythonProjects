__author__   = "Justin Iravani"

import MySQLdb

source = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
target = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

source_cursor = source.cursor()
target_cursor = target.cursor()

source_cursor.execute("SELECT * FROM mls_dw.DiM_pOtAtO;")

results = source_cursor.fetchall()

for row in results:
    sql = """INSERT INTO `mls_dw`.`event_fact`
            (`event_id`,`prim_player_id`,`sec_player_id`,`prim_team_id`,`sec_team_id`,
             `date_id`,`time_id`,`event_type_id`,`game_id`)
            VALUES
            (%d,%d,%d,%d,%d,%d,%d,%d);""" % (row)


    try:
        target_cursor.execute(sql)
        target.commit()
    except:
        target.rollback()

source.close()
target.close()
