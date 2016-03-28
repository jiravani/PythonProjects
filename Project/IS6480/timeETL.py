__author__   = "Justin Iravani"

import MySQLdb
import math

# final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")
# final_cursor = final.cursor()

for x in xrange(1,3):
    for y in xrange(0,3601):
        seconds = float(y)
        minutes = seconds / 60
        fminutes =  "{:0>2}".format(int(minutes))
        fseconds = ":{:0>2}".format(int(seconds % 60))

        sql = "INSERT INTO `mls_dw`.`dim_time` (`period`,`seconds`,`minutes`) VALUES (%d,%s,\"%s%s\");" \
              % (x,
                 "{}".format(int(seconds)),
                 fminutes,fseconds)
        print sql
        # try:
        #     final_cursor.execute(sql)
        #     final.commit()
        # except:
        #     final.rollback()

# final.close()

# if int(seconds % 60) < 10:
#             sql = "INSERT INTO `mls_dw`.`dim_time`(`seconds`,`minutes`,`formatted_time`) VALUES (" \
#                   "{string}".format(string=seconds) + \
#                   "," \
#                   "{string}".format(string=minutes) + \
#                   ",\"" + \
#                   "{string}".format(string=int(minutes)) + \
#                   ":0" + \
#                   "{string}".format(string=int(seconds % 60)) + "\");"
#         else:
#             sql = "INSERT INTO `mls_dw`.`dim_time`(`seconds`,`minutes`,`formatted_time`) VALUES (" + \
#                   "{string}".format(string=seconds) + \
#                   "," \
#                   "{string}".format(string=minutes) + \
#                   ",\"" + \
#                   "{string}".format(string=int(minutes)) + \
#                   ":" + \
#                   "{string}".format(string=int(seconds % 60)) + "\");"