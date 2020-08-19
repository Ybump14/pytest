import os, sys, requests
import time
import pytest

sys.path.append(os.getcwd())
from utils.commlib import get_test_data, res_validate, get_request

cases, parameters = get_test_data(
    "E:/110_pytest/data/carSalesDetailReport.yml",
    "E:/110_pytest/data/repairOrderDetailReport.yml",
    "E:/110_pytest/data/activityRepairPackageOrder.yml",
    "E:/110_pytest/data/externalAccessoriesOrder.yml",
    "E:/110_pytest/data/externalBoutiqueOrder.yml",
    "E:/110_pytest/data/accessoriesReceiveOrderDetailReport.yml",
    "E:/110_pytest/data/boutiqueReceiveOrderDetailReport.yml",
    "E:/110_pytest/data/insuranceOrderDetailReport.yml",
    "E:/110_pytest/data/团队管理.yml", "E:/110_pytest/data/客户管理.yml",
    "E:/110_pytest/data/客服管理.yml", "E:/110_pytest/data/配件管理.yml",
    "E:/110_pytest/data/精品管理.yml", "E:/110_pytest/data/车辆管理.yml",
    "E:/110_pytest/data/车辆销售管理.yml", "E:/110_pytest/data/维修接待管理.yml",
    "E:/110_pytest/data/保险管理.yml", "E:/110_pytest/data/营销管理.yml",
    "E:/110_pytest/data/外销_内部领件管理.yml", "E:/110_pytest/data/收款管理.yml",
    "E:/110_pytest/data/开票管理.yml", "E:/110_pytest/data/财务管理.yml",
    "E:/110_pytest/data/参数_权限_系统管理.yml"
)
list_params = list(parameters)


class Test_List(object):
    @pytest.mark.parametrize("name,http,validate", list_params, ids=cases)
    def test_List(self, env, name, http, validate, token):
        r = get_request(env=env, name=name, http=http, token=token)
        res_validate(data=r.json(), validate=validate, status_code=r.status_code)
