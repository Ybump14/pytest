import json
import os, requests
import time

import yaml
import pytest
from utils.commlib import decode
from filelock import FileLock


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
def token_oa(env, tmp_path_factory, worker_id):
    url1 = env["data"]["url1"]
    url_oa = env["data"]["url_oa"]
    url = url1 + url_oa
    data = {
        "loginNum": env["data"]["username"],
        "password": env["data"]["password"]
    }
    if worker_id == "master":
        r = requests.post(url=url, json=data)
        res = r.json()
        if "randomId" in res:
            response = decode(res["randomId"], res["encryptData"])
            res = json.loads(response)
        token = res["data"]["token"]
        os.environ["token"] = token
        return os.environ["token"]

    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            token = json.loads(fn.read_text())
            os.environ["token"] = token
        else:
            r = requests.post(url=url, json=data)
            res = r.json()
            if "randomId" in res:
                response = decode(res["randomId"], res["encryptData"])
                res = json.loads(response)
            token = res["data"]["token"]
            fn.write_text(json.dumps(token))
            os.environ["token"] = token
    return os.environ["token"]


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
    res = r.json()
    if "randomId" in res:
        response = decode(res["randomId"], res["encryptData"])
        res = json.loads(response)
    token = res["data"]["token"]
    return token


def parameters_request(env, parameters, token, Environmental=None):
    headers = parameters["request"]["headers"]
    headers["Authorization"] = token
    headers["Timestamp"] = str(round(time.time()) * 1000)
    requests.adapters.DEFAULT_RETRIES = 5
    r = requests.session()
    r.keep_alive = False
    if Environmental in 'oa':
        r = requests.request(parameters["request"]["method"], url=env["data"]["url1"] + parameters['name'],
                             headers=headers,
                             json=parameters["request"]["data"])
    else:
        r = requests.request(parameters["request"]["method"], url=env["data"]["url2"] + parameters['name'],
                             headers=headers,
                             json=parameters["request"]["data"])
    if r.status_code == 200:
        res_validate(r.json(), parameters["validate"], r.status_code)
    else:
        raise TypeError('the response status.code is %s' % r.status_code)
    return r


def res_validate(data, validate, status_code):
    if "randomId" in data:
        response = decode(data["randomId"], data["encryptData"])
        data = json.loads(response)
    assert data["code"] == validate["code"]
    assert data["msg"] == validate["msg"]
    assert status_code == validate["status"]
