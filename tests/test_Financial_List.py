import pytest

from tests.conftest import parameters_request


class Test_Financial_List():

    @pytest.mark.datafile("data/financial/financialTreatment.yml")
    def test_financialTreatment(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

    @pytest.mark.datafile("data/financial/fixedAssets.yml")
    def test_fixedAssets(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

    @pytest.mark.datafile("data/financial/businessBookkeeping.yml")
    def test_businessBookkeeping(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

    @pytest.mark.datafile("data/financial/authorityManagement.yml")
    def test_authorityManagement(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

    @pytest.mark.datafile("data/financial/parameterManagement.yml")
    def test_parameterManagement(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

    @pytest.mark.datafile("data/financial/financialStatements.yml")
    def test_financialStatements(self, env, parameters, token_financial):
        parameters_request(env, parameters, token_financial, Environmental='financial')

if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_List.py'])
    pytest.main(['-v', '-s', '--env', 'test', 'test_Financial_List.py'])

# pytest tests/test_List.py -v -n auto 多线程
# pytest tests/test_List.py -v  单线程
