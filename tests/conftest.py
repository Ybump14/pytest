import inspect
import json
import os, requests
import allure
import yaml
import pytest
from _pytest import logging
from _pytest.assertion.util import assertrepr_compare
from utils.commlib import decode


def pytest_generate_tests(metafunc):
    ids = []
    markers = metafunc.definition.own_markers
    for marker in markers:
        if marker.name == 'datafile':
            test_data_path = os.path.join(metafunc.config.rootdir, marker.args[0])
            with open(test_data_path, 'r', encoding='utf-8') as f:
                ext = os.path.splitext(test_data_path)[-1]
                if ext in ['.yaml', '.yml']:
                    test_data = yaml.load(f.read(), Loader=yaml.SafeLoader)
                elif ext in ['.json']:
                    test_data = json.load(f)
                else:
                    raise TypeError('datafile must be yaml or json,root must be tests')
    if "parameters" in metafunc.fixturenames:
        for data in test_data['teststeps']:
            ids.append(data['name'])
        metafunc.parametrize("parameters", test_data['teststeps'], ids=ids, scope="function")


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="110",
                     help="environment: 110 or test")


@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config


@pytest.fixture(scope="session")
def token_oa(env):
    url1 = env["data"]["url1"]
    url_oa = env["data"]["url_oa"]
    url = url1 + url_oa
    data = {
        "loginNum": env["data"]["username"],
        "password": env["data"]["password"]
    }
    r = requests.post(url=url, json=data)
    if "randomId" in r.json():
        response = decode(r.json()["randomId"], r.json()["encryptData"])
        res = json.loads(response)
        token = res["data"]["token"]
        return token
    else:
        res = r.json()
        token = res["data"]["token"]
        return token


@pytest.fixture(scope="session")
def token_financial(env):
    url1 = env["data"]["url2"]
    url_financial = env["data"]["url_financial"]
    url = url1 + url_financial
    data = {
        "loginNum": env["data"]["username"],
        "password": env["data"]["password"]
    }
    r = requests.post(url=url, json=data)
    if "randomId" in r.json():
        response = decode(r.json()["randomId"], r.json()["encryptData"])
        res = json.loads(response)
        token = res["data"]["token"]
        return token
    else:
        res = r.json()
        token = res["data"]["token"]
        return token


def pytest_assertrepr_compare(config, op, left, right):
    left_name, right_name = inspect.stack()[7].code_context[0].lstrip().lstrip('assert').rstrip('\n').split(op)
    pytest_output = assertrepr_compare(config, op, left, right)
    logging.debug("{0} is\n {1}".format(left_name, left))
    logging.debug("{0} is\n {1}".format(right_name, right))
    with allure.step("校验结果"):
        allure.attach(str(left), left_name)
        allure.attach(str(right), right_name)
    return pytest_output
