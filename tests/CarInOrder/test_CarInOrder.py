import os, sys
import pytest

from utils.mysql_connect import MySql

sys.path.append(os.getcwd())
from utils.commlib import res_validate, parameters_request

vin = None
expressNo = None


class Test_CarInOrder(object):

    @pytest.mark.run(order=1)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderSave.yml")
    def test_CarInOrderSave(self, env, parameters, token):
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)
        global vin
        global expressNo
        vin = parameters["request"]['data']['carInOrderDetails'][0]['vin']
        expressNo = parameters["request"]['data']['expressNo']

    @pytest.mark.run(order=2)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderAudit.yml")
    def test_CarInOrderAudit(self, env, parameters, token):
        carInOrderId = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        parameters["request"]['data']['carInOrderId'] = db.mysql_select(carInOrderId)
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.run(order=3)
    @pytest.mark.datafile("110_data/CarInOrder/CarInStock.yml")
    def test_CarInStock(self, env, parameters, token):
        carInOrderId = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        carInOrderDetails = "SELECT id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        parameters["request"]['data']['carInOrderId'] = db.mysql_select(carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['id'] = db.mysql_select(carInOrderDetails)
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.run(order=4)
    @pytest.mark.datafile("110_data/CarInOrder/CarInOrderFinalAudit.yml")
    def test_CarInOrderFinalAudit(self, env, parameters, token):
        carInOrderId = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        carInOrderDetails = "SELECT id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        parameters["request"]['data']['carInOrderId'] = db.mysql_select(carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['carInOrderDetailId'] = db.mysql_select(carInOrderDetails)
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
