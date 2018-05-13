import MySQLdb

# 获取链接
try:
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='',
        db='test',
        port=3306,
        charset='utf8'
    )
except MySQLdb.Error as e:
    print('Error: %s' % e)

# 获取数据    
cursor = conn.cursor()
cursor.execute('SELECT * FROM `pets` ORDER BY `name` DESC')
rest = cursor.fetchone()

print(rest)

conn.close()
