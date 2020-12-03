import cx_Oracle

db = cx_Oracle.connect('ocean_arch', 'sea3000', '192.168.176.25:1521/sea')
print(db.version)

cursor = db.cursor()
try:
    cursor.execute('select * from E_FRONT_SERVER_MSG_CNT')
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
except Exception as e:
    print(e)