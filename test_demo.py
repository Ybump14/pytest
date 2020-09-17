## -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class car_in_order_details(Base):
    __tablename__ = 'car_in_order_details'

    id = Column(String, primary_key=True)
    vin = Column(String)
    car_in_order_id = Column(String)

    def __repr__(self):
        return "<User(id='%s', car_in_order_id='%s',vin='%s')>" % (
            self.id, self.car_in_order_id, self.vin)


class car_stock(Base):
    __tablename__ = 'car_stock'

    id = Column(String, primary_key=True)
    vin = Column(String)

    def __repr__(self):
        return "<User(id='%s',vin='%s')>" % (
            self.id, self.vin)
