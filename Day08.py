import cx_Oracle

db = cx_Oracle.connect('ocean_arch', 'sea3000', '192.168.176.25:1521/sea')
print(db.version)

cursor = db.cursor()
try:
    bool = cursor.execute('select * from E_FRONT_SERVER_MSG_CNT')
    print(bool)
except Exception:
    print(cx_Oracle.DatabaseError)