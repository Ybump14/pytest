import os, sys
import pytest

from models.CarInOrder import car_in_order_details
from utils.Sql_connect import sql_connect
from utils.mysql_connect import MySql

sys.path.append(os.getcwd())
from utils.commlib import parameters_request, Publice

vin = None
expressNo = None
carInOrderId = None
carInOrderDetails = None
contractId = None
get_vin = Publice()


class Test_CarInOrder(object):

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=1)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderSave.yml")
    def test_CarInOrderSave(self, env, parameters, token):
        global vin
        global expressNo
        global carInOrderId
        global carInOrderDetails
        session = sql_connect()
        parameters["request"]['data']['carInOrderDetails'][0]['vin'] = get_vin.ranstr(17)
        parameters["request"]['data']['expressNo'] = get_vin.ranlong(6)
        parameters_request(env, parameters, token)
        vin = parameters["request"]['data']['carInOrderDetails'][0]['vin']
        expressNo = parameters["request"]['data']['expressNo']
        carInOrderId = session.query(car_in_order_details).filter(
            car_in_order_details.vin == vin).first().car_in_order_id
        carInOrderDetails = session.query(car_in_order_details).filter(
            car_in_order_details.vin == vin).first().id

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=2)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderAudit.yml")
    def test_CarInOrderAudit(self, env, parameters, token):
        parameters["request"]['data']['carInOrderId'] = carInOrderId
        parameters_request(env, parameters, token)

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=3)
    @pytest.mark.datafile("110_data/carInOrder/CarInStock.yml")
    def test_CarInStock(self, env, parameters, token):
        parameters["request"]['data']['carInOrderId'] = (carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['id'] = (carInOrderDetails)
        parameters_request(env, parameters, token)

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=4)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderFinalAudit.yml")
    def test_CarInOrderFinalAudit(self, env, parameters, token):
        parameters["request"]['data']['carInOrderId'] = (carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['carInOrderDetailId'] = (carInOrderDetails)
        parameters_request(env, parameters, token)

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=5)
    def test_DeleteDate(self):
        sql = ("DELETE FROM car_in_order_details WHERE vin = '%s'" % vin,
               "DELETE FROM car_in_order WHERE express_no = '%s'" % expressNo,
               "DELETE FROM car_info WHERE vin = '%s'" % vin,
               "DELETE FROM car_stock WHERE vin = '%s'" % vin)
        db = MySql()
        db.mysql_update(sql)

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=6)
    @pytest.mark.datafile("110_data/carInOrder/CarSalesContractSave.yml")
    def test_CarSalesContractSave(self, env, parameters, token):
        r = parameters_request(env, parameters, token)
        global contractId
        contractId = r.json()['data']['id']

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=7)
    @pytest.mark.datafile("110_data/carInOrder/CarSalesContractAudit.yml")
    def test_CarSalesContractAudit(self, env, parameters, token):
        parameters['request']['data']['contractId'] = contractId
        parameters_request(env, parameters, token)

    # @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=8)
    @pytest.mark.datafile("110_data/carInOrder/contractAssgnationCarOrReleaseCar.yml")
    def test_contractAssgnationCarOrReleaseCar(self, env, parameters, token):
        sql = ("SELECT id FROM car_info WHERE vin = '%s'" % vin)
        db = MySql()
        carInfoId = db.mysql_select(sql)
        parameters['request']['data']['contractId'] = contractId
        parameters['request']['data']['carInfoId'] = carInfoId
        parameters_request(env, parameters, token)
