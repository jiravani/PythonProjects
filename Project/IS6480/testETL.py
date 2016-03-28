
import MySQLdb

source = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
target = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

source_cursor = source.cursor()
target_cursor = target.cursor()

source_cursor.execute("SELECT * FROM source_table;")

results = source_cursor.fetchall()

for row in results:
    sql = """INSERT INTO target_table (`var1`,`var2`,...) VALUES (%d,%d,....);""" % (row)
    try:
        target_cursor.execute(sql)
        target.commit()
    except:
        target.rollback()

source.close()
target.close()
