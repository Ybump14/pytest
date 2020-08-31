import os, sys
import pytest

from test_demo import car_in_order_details
from utils.Sql_connect import sql_connect
from utils.mysql_connect import MySql

sys.path.append(os.getcwd())
from utils.commlib import res_validate, parameters_request

vin = None
expressNo = None
carInOrderId = None
carInOrderDetails = None


class Test_CarInOrder(object):

    @pytest.mark.run(order=1)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderSave.yml")
    def test_CarInOrderSave(self, env, parameters, token):
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)
        global vin
        global expressNo
        global carInOrderId
        global carInOrderDetails
        vin = parameters["request"]['data']['carInOrderDetails'][0]['vin']
        expressNo = parameters["request"]['data']['expressNo']
        session = sql_connect()
        carInOrderId = session.query(car_in_order_details).filter(
            car_in_order_details.vin == vin).first().car_in_order_id
        carInOrderDetails = session.query(car_in_order_details).filter(
            car_in_order_details.vin == vin).first().id

    @pytest.mark.run(order=2)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderAudit.yml")
    def test_CarInOrderAudit(self, env, parameters, token):
        parameters["request"]['data']['carInOrderId'] = carInOrderId
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.run(order=3)
    @pytest.mark.datafile("110_data/CarInOrder/CarInStock.yml")
    def test_CarInStock(self, env, parameters, token):
        db = MySql()
        parameters["request"]['data']['carInOrderId'] = (carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['id'] = (carInOrderDetails)
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.run(order=4)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderFinalAudit.yml")
    def test_CarInOrderFinalAudit(self, env, parameters, token):
        db = MySql()
        parameters["request"]['data']['carInOrderId'] = (carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['carInOrderDetailId'] = (carInOrderDetails)
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.run(order=5)
    def test_DeleteDate(self):
        sql = ("DELETE FROM car_in_order_details WHERE vin = '%s'" % vin,
               "DELETE FROM car_in_order WHERE express_no = '%s'" % expressNo,
               "DELETE FROM car_info WHERE vin = '%s'" % vin,
               "DELETE FROM car_stock WHERE vin = '%s'" % vin)
        db = MySql()
        db.mysql_update(sql)
