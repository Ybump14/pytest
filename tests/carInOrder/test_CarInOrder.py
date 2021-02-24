import pytest
from models.CarInOrder import car_in_order_details
from utils.Sql_connect import sql_connect
from utils.mysql_connect import MySql
from utils.commlib import Util
from tests.conftest import parameters_request


# vin = None
# expressNo = None
# carInOrderId = None
# carInOrderDetails = None
# contractId = None


class Test_CarInOrder(object):
    vin = None
    expressNo = None
    carInOrderId = None
    carInOrderDetails = None
    contractId = None

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=1)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderSave.yml")
    def test_CarInOrderSave(self, env, parameters, token_oa):
        # global vin
        # global expressNo
        # global carInOrderId
        # global carInOrderDetails
        session = sql_connect()
        parameters["request"]['data']['carInOrderDetails'][0]['vin'] = Util.ranstr(17)
        parameters["request"]['data']['expressNo'] = Util.ranlong(6)
        parameters_request(env, parameters, token_oa, Environmental='oa')
        Test_CarInOrder.vin = parameters["request"]['data']['carInOrderDetails'][0]['vin']
        Test_CarInOrder.expressNo = parameters["request"]['data']['expressNo']
        Test_CarInOrder.carInOrderId = session.query(car_in_order_details).filter(
            car_in_order_details.vin == Test_CarInOrder.vin).first().car_in_order_id
        Test_CarInOrder.carInOrderDetails = session.query(car_in_order_details).filter(
            car_in_order_details.vin == Test_CarInOrder.vin).first().id

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=2)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderAudit.yml")
    def test_CarInOrderAudit(self, env, parameters, token_oa):
        parameters["request"]['data']['carInOrderId'] = Test_CarInOrder.carInOrderId
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=3)
    @pytest.mark.datafile("110_data/carInOrder/CarInStock.yml")
    def test_CarInStock(self, env, parameters, token_oa):
        parameters["request"]['data']['carInOrderId'] = (Test_CarInOrder.carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['id'] = (Test_CarInOrder.carInOrderDetails)
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=4)
    @pytest.mark.datafile("110_data/carInOrder/CarInOrderFinalAudit.yml")
    def test_CarInOrderFinalAudit(self, env, parameters, token_oa):
        parameters["request"]['data']['carInOrderId'] = (Test_CarInOrder.carInOrderId)
        parameters["request"]['data']['carInOrderDetails'][0]['carInOrderDetailId'] = (
            Test_CarInOrder.carInOrderDetails)
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=5)
    def test_DeleteDate(self):
        sql = ("DELETE FROM car_in_order_details WHERE vin = '%s'" % Test_CarInOrder.vin,
               "DELETE FROM car_in_order WHERE express_no = '%s'" % Test_CarInOrder.expressNo,
               "DELETE FROM car_info WHERE vin = '%s'" % Test_CarInOrder.vin,
               "DELETE FROM car_stock WHERE vin = '%s'" % Test_CarInOrder.vin)
        db = MySql()
        db.mysql_update(sql)

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=6)
    @pytest.mark.datafile("110_data/carInOrder/CarSalesContractSave.yml")
    def test_CarSalesContractSave(self, env, parameters, token_oa):
        r = parameters_request(env, parameters, token_oa, Environmental='oa')
        # global contractId
        Test_CarInOrder.contractId = r.json()['data']['id']

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=7)
    @pytest.mark.datafile("110_data/carInOrder/CarSalesContractAudit.yml")
    def test_CarSalesContractAudit(self, env, parameters, token_oa):
        parameters['request']['data']['contractId'] = Test_CarInOrder.contractId
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.skip(reason='test')
    @pytest.mark.run(order=8)
    @pytest.mark.datafile("110_data/carInOrder/contractAssgnationCarOrReleaseCar.yml")
    def test_contractAssgnationCarOrReleaseCar(self, env, parameters, token_oa):
        sql = ("SELECT id FROM car_info WHERE vin = '%s'" % Test_CarInOrder.vin)
        db = MySql()
        carInfoId = db.mysql_select(sql)
        parameters['request']['data']['contractId'] = Test_CarInOrder.contractId
        parameters['request']['data']['carInfoId'] = carInfoId
        parameters_request(env, parameters, token_oa, Environmental='oa')


if __name__ == '__main__':
    pytest.main(['-v', 'test_CarInOrder.py'])
