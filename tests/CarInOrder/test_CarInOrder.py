import os, sys, requests
import pytest

from utils.mysql_connect import MySql

sys.path.append(os.getcwd())
from utils.commlib import get_test_data, res_validate, get_headers, get_request

CarInOrderSave_cases, CarInOrderSave_parameters = get_test_data("E:/110_pytest/110_data/CarInOrder/CarInOrderSave.yml")
CarInOrderAudit_cases, CarInOrderAudit_parameters = get_test_data("E:/110_pytest/110_data/CarInOrder/CarInOrderAudit.yml")
CarInStock_cases, CarInStock_parameters = get_test_data("E:/110_pytest/110_data/CarInOrder/CarInStock.yml")
CarInOrderFinalAudit_cases, CarInOrderFinalAudit_parameters = get_test_data("E:/110_pytest/110_data/CarInOrder/CarInOrderFinalAudit.yml")

CarInStock_list_params = list(CarInStock_parameters)
CarInOrderSave_list_params = list(CarInOrderSave_parameters)
CarInOrderAudit_list_params = list(CarInOrderAudit_parameters)
CarInOrderFinalAudit_list_params = list(CarInOrderFinalAudit_parameters)

class Test_CarInOrder(object):
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,http,validate", CarInOrderSave_list_params, ids=CarInOrderSave_cases)
    def test_CarInOrderSave(self, env, name, http, validate, token):
        headers = get_headers(http, token)
        r = get_request(env, name, http, headers)
        res_validate(r.json(), validate, r.status_code)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,http,validate", CarInOrderAudit_list_params, ids=CarInOrderAudit_cases)
    def test_CarInOrderAudit(self, env, name, http, validate, token):
        headers = get_headers(http, token)
        vin = 'XXXXX202008101557'
        sql = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        http['data']['carInOrderId'] = db.mysql_select(sql)
        r = get_request(env, name, http, headers)
        res_validate(r.json(), validate, r.status_code)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("name,http,validate", CarInStock_list_params, ids=CarInStock_cases)
    def test_CarInStock(self, env, name, http, validate, token):
        headers = get_headers(http, token)
        vin = 'XXXXX202008101557'
        carInOrderId = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        carInOrderDetails = "SELECT id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        http['data']['carInOrderId'] = db.mysql_select(carInOrderId)
        http['data']['carInOrderDetails'][0]['id'] = db.mysql_select(carInOrderDetails)
        r = get_request(env, name, http, headers)
        res_validate(r.json(), validate, r.status_code)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("name,http,validate", CarInOrderFinalAudit_list_params, ids=CarInOrderFinalAudit_cases)
    def test_CarInOrderFinalAudit(self, env, name, http, validate, token):
        headers = get_headers(http, token)
        vin = 'XXXXX202008101557'
        carInOrderId = "SELECT car_in_order_id FROM car_in_order_details where vin = '%s'" % vin
        carInOrderDetails = "SELECT id FROM car_in_order_details where vin = '%s'" % vin
        db = MySql()
        http['data']['carInOrderId'] = db.mysql_select(carInOrderId)
        http['data']['carInOrderDetails'][0]['carInOrderDetailId'] = db.mysql_select(carInOrderDetails)
        r = get_request(env, name, http, headers)
        res_validate(r.json(), validate, r.status_code)
