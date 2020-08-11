import json
import os, sys, requests
import time

import yaml
import pytest

sys.path.append(os.getcwd())
from utils.commlib import decode


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
def token(env):
    url1 = env["data"]["url"]
    url2 = "/api/staff/login.json"
    url = url1 + url2
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





#
# def pytest_assertrepr_compare(config, op, left, right):
#     left_name, right_name = inspect.stack()[7].code_context[0].lstrip().lstrip('assert').rstrip('\n').split(op)
#     pytest_output = assertrepr_compare(config, op, left, right)
#     logging.debug("{0} is\n {1}".format(left_name, left))
#     logging.debug("{0} is\n {1}".format(right_name, right))
#     with allure.step("校验结果"):
#         allure.attach(str(left), left_name)
#         allure.attach(str(right), right_name)
#     return pytest_output
