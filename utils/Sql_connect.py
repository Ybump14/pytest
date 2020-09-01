## -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def sql_connect():
    # 创建数据库连接
    engine = create_engine("mysql://root:root@192.168.1.110:3306/yr-sw-oa?charset=utf8",
                           encoding='utf-8',
                           max_overflow=0,
                           pool_size=5,
                           pool_timeout=30,
                           pool_recycle=-1)
    # 创建DBSession类型
    DBSession = sessionmaker(bind=engine)
    # 创建session对象
    session = DBSession()
    return session
