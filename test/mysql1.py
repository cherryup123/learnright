# -*- coding: utf-8 -*

import MySQLdb

conn = MySQLdb.connect(host='192.168.2.27', user='www',passwd='wealink.com',db='s2c',charset='utf8')

cursor = conn.cursor()
count = cursor.execute('select * from user')
print "只获取一条记录:"
# result = cursor.fetchone();
# print result
# print type(result)
# print result[0]
#
# list1={'uid':result[0],'mobile':result[1]}
# print list1


index=cursor.description
result =[]
for res in cursor.fetchall():
    row={}
    for i in range(len(index)-1):
        row[index[i][0]]=res[i]
    result.append(row)
print result
print result[0]
print (result[0]['uid'])
