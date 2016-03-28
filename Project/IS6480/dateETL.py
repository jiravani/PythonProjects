__author__   = "Justin Iravani"

import MySQLdb
import datetime

def insert(dateObj):

    item = dateObj
    assert isinstance(item, datetime.datetime)

    year = item.year
    month = item.month
    day = item.day
    quarter = (item.month-1)/3+1
    is_holiday = 1 if (item.weekday() > 4) else 0

    sql = "INSERT INTO `mls_dw`.`dim_date`(`date`,`year`,`quarter`,`month`,`day`,`day_of_week`,`is_holiday`) " \
          "VALUES (%s,%s,%s,%s,%s,%s,%s)" \
          % ("'{date}'".format(date = item.date()),year, quarter, month, day,
          "{weekday}".format(weekday = item.weekday()),is_holiday)
    print sql
    # try:
    #     # Execute the SQL command
    #     final_cursor.execute(sql)
    #     # Commit your changes in the database
    #     final.commit()
    # except:
    #     # Rollback in case there is any error
    #     print "error"
    #     final.rollback()

# Open database connection
raw = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
final = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

raw_cursor = raw.cursor()
final_cursor = final.cursor()

raw_cursor.execute("SELECT distinct game_date_gen FROM mls_data_raw.events UNION SELECT distinct game_date_gen FROM"
                   " mls_data_raw.locations order by game_date_gen;")
results = raw_cursor.fetchall()

for row in results:
    for item in row:
        insert(item)

# Close database connection
raw.close()
final.close()