# -*- coding: UTF-8 -*-
import mysql.connector
import traceback


class MySql(object):

    def mysql_connect(self):
        db = mysql.connector.connect(
            host="192.168.1.110",
            user="root",
            passwd="root",
            database="yr-sw-oa",
            auth_plugin='mysql_native_password'
        )
        return db

    def mysql_select(self,sql):
        get_connect = MySql()
        db = get_connect.mysql_connect()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
        finally:
            cursor.close()
            db.close()
            return data

    def mysql_update(self,sql,var):
        get_connect = MySql()
        db = get_connect.mysql_connect()
        try:
            cursor = db.cursor()
            cursor.execute(sql,var)
            db.commit()
            print("更新成功")
        except Exception as e:
            traceback.print_exc()
            db.rollback()
        finally:
            cursor.close()
            db.close()






