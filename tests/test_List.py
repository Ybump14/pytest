import pytest

from tests.conftest import parameters_request


class Test_List():

    @pytest.mark.datafile("data/oa/carSalesDetailReport.yml")
    def test_carSalesDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/repairOrderDetailReport.yml")
    def test_repairOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/activityRepairPackageOrder.yml")
    def test_activityRepairPackageOrder(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/externalAccessoriesOrder.yml")
    def test_externalAccessoriesOrder(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/externalBoutiqueOrder.yml")
    def test_externalBoutiqueOrder(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/accessoriesReceiveOrderDetailReport.yml")
    def test_accessoriesReceiveOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/boutiqueReceiveOrderDetailReport.yml")
    def test_boutiqueReceiveOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/insuranceOrderDetailReport.yml")
    def test_insuranceOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/otherReceiveOrderDetailReport.yml")
    def test_otherReceiveOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/carRedemOrderFinancingReport.yml")
    def test_otherReceiveOrderDetailReport(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/teamManagement.yml")
    def test_teamManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/customerManagement.yml")
    def test_customerManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/customerServiceManagement.yml")
    def test_customerServiceManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/partsManagement.yml")
    def test_partsManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/boutiqueManagement.yml")
    def test_boutiqueManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/vehicleManagement.yml")
    def test_vehicleManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/vehicleSaleManagement.yml")
    def test_vehicleSaleManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/repairReceptionManagement.yml")
    def test_repairReceptionManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/insuranceManagement.yml")
    def test_insuranceManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/marketingManagement.yml")
    def test_marketingManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/external_take_Management.yml")
    def test_external_take_Management(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/receiptManagement.yml")
    def test_receiptManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/ticketManagement.yml")
    def test_ticketManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/financeManagement.yml")
    def test_financeManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')

    @pytest.mark.datafile("data/oa/parameter_auth_systemManagement.yml")
    def test_parameter_auth_systemManagement(self, env, parameters, token_oa):
        parameters_request(env, parameters, token_oa, Environmental='oa')


if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_List.py'])
    pytest.main(['-v', '-s', '--env', 'test', 'test_List.py'])

# pytest tests/test_List.py -v -n auto 多线程
# pytest tests/test_List.py -v  单线程
