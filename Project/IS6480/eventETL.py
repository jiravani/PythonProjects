__author__   = "Justin Iravani"

import MySQLdb


raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()

raw_cursor.execute("SELECT distinct event_type FROM mls_data_raw.events ORDER BY event_type;")

results = raw_cursor.fetchall()

for row in results:
    sql ="INSERT INTO `mls_dw`.`dim_event_type`(`type`) VALUES (\"%s\");" % (row)


    try:
        final_cursor.execute(sql)
        final.commit()
    except:

        final.rollback()
raw.close()
final.close()
