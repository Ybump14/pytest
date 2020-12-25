import os, sys
import pytest

sys.path.append(os.getcwd())
from utils.commlib import res_validate, parameters_request


class Test_List():

    def run_request(self, env, parameters, token):
        r = parameters_request(env, parameters, token)
        res_validate(r.json(), parameters["validate"], r.status_code)

    @pytest.mark.datafile("data/carSalesDetailReport.yml")
    def test_carSalesDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/repairOrderDetailReport.yml")
    def test_repairOrderDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/activityRepairPackageOrder.yml")
    def test_activityRepairPackageOrder(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/externalAccessoriesOrder.yml")
    def test_externalAccessoriesOrder(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/externalBoutiqueOrder.yml")
    def test_externalBoutiqueOrder(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/accessoriesReceiveOrderDetailReport.yml")
    def test_accessoriesReceiveOrderDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/boutiqueReceiveOrderDetailReport.yml")
    def test_boutiqueReceiveOrderDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/insuranceOrderDetailReport.yml")
    def test_insuranceOrderDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/teamManagement.yml")
    def test_teamManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/customerManagement.yml")
    def test_customerManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/customerServiceManagement.yml")
    def test_customerServiceManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/partsManagement.yml")
    def test_partsManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/boutiqueManagement.yml")
    def test_boutiqueManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/vehicleManagement.yml")
    def test_vehicleManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/vehicleSaleManagement.yml")
    def test_vehicleSaleManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/repairReceptionManagement.yml")
    def test_repairReceptionManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/insuranceManagement.yml")
    def test_insuranceManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/marketingManagement.yml")
    def test_marketingManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/external_take_Management.yml")
    def test_external_take_Management(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/receiptManagement.yml")
    def test_receiptManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/otherReceiveOrderDetailReport.yml")
    def test_otherReceiveOrderDetailReport(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/ticketManagement.yml")
    def test_ticketManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/financeManagement.yml")
    def test_financeManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)

    @pytest.mark.datafile("data/parameter_auth_systemManagement.yml")
    def test_parameter_auth_systemManagement(self, env, parameters, token):
        Test_List.run_request(self, env, parameters, token)
