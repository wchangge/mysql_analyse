import sys
import os
import mysql.connector as con
print(os.system('python -V'))

mydb = con.connect(
    host = '172.16.100.230',
    port = 3399,
    user = 'hansight',
    passwd = 'hansight',
    database = 'mysql_analyse')

mycursor = mydb.cursor()
mycursor.execute('show tables')
for x in mycursor:
    print(x)

insert_line = 'insert into table1 (key1,key2,value1) values (%s,%s,%s)'
#为什么加个%d就有问题?
val = ('004','004','1311232')
mycursor.execute(insert_line,val)
mydb.commit()
print(mydb)