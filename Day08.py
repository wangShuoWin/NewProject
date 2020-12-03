# import cx_Oracle
#
# db = cx_Oracle.connect('ocean_arch', 'sea3000', '192.168.176.25:1521/sea')
# print(db.version)
#
# cursor = db.cursor()
# try:
#     bool = cursor.execute('select * from E_FRONT_SERVER_MSG_CNT')
#     print(bool)
# except Exception:
#     print(cx_Oracle.DatabaseError)




#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: XXX
# @Time: 2020/11/17
# @Desc: 数据接口-oracle操作类
import cx_Oracle as cx
import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'


class DIOracle(object):
    def __init__(self, username, pwd, ip, port, sid):
        # 实例属性
        self.__username = username
        self.__pwd = pwd
        self.__ip = ip
        self.__port = port
        self.__sid = sid
        self.__connection = None
        self.conn_flag = False

    # 连接数据库。私有方法，不用显式调用
    def __connect_db(self):
        # 之前为连接状态，需要进一步确认中途是否已断开连接
        if self.conn_flag is True:
            try:
                cr = self.__connection.cursor()
                cr.execute("select 1 from dual")
                # 连接还有效，直接返回
                return True
            except Exception as e:
                print(e)
                # 连接已经无效了，置标志，下面会进行重连
                self.__connection.close()
                self.conn_flag = False

        # 进行数据库连接
        try:
            lsnr = self.__ip+":"+self.__port+"/"+self.__sid
            self.__connection = cx.connect(self.__username, self.__pwd, lsnr)
            self.conn_flag = True
            return True
        except Exception as e:
            print(e)
            return False

    # 查询纪录
    def sql_select(self, sql):
        flag = self.__connect_db()
        if flag is False:
            return

        try:
            cr = self.__connection.cursor()
            cr.execute(sql)
            rs = cr.fetchall()
            cr.close()
            return rs
        except Exception as e:
            print(e)
            self.close_db()
            return

    # 增删改纪录
    def sql_dml(self, sql):
        flag = self.__connect_db()
        if flag is False:
            return False

        try:
            cr = self.__connection.cursor()
            cr.execute(sql)
            cr.close()
            self.__connection.commit()
            return True
        except Exception as e:
            print(e)
            self.close_db()
            return False

    # 连接数据库
    def close_db(self):
        if self.conn_flag is False:
            return

        self.__connection.close()
        self.conn_flag = False

test = DIOracle('ocean_arch',"sea3000","192.168.176.25","1521",'sea')
sql='select * from test_cc'
res = test.sql_select(sql)
print(res)
