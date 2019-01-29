import pymysql

db = pymysql.connect(host = '172.16.100.230', port = 3399, user = 'hansight', passwd = 'hansight', db = 'mysql_analyse')
cusor = db.cursor()

sql = 'insert into table1 (key1,key2,value1) values (\'007\',\'007\',23373)'
sql2 = 'select * from table1'
try:
    cusor.execute(sql)
    db.commit()
except:
    db.rollback()

try:
    cusor.execute(sql2)
    db.commit()
except:
    db.rollback()

db.close()