__author__   = "Justin Iravani"

import MySQLdb


raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()

raw_cursor.execute("SELECT distinct event_type FROM mls_data_raw.events ORDER BY event_type;")
results = raw_cursor.fetchall()

for row in results:
    for item in row:
        s = "{string}".format(string = item)
        print s
        try:
            # Execute the SQL command
            final_cursor.execute("INSERT INTO `mls_dw`.`event`(`type`) VALUES (\"" + s + "\");")
            # Commit your changes in the database
            final.commit()
        except:
            # Rollback in case there is any error
            print "error"
            final.rollback()

raw.close()
final.close()
