>环境准备

- 安装pytest
```
pip install pytest
```
- 安装har2case
```
pip install har2case
```
- 安装allure
```
pip install allure-pytest
```
<!-- more -->

---

**以下为执行步骤说明和相关指令**

---

执行步骤示例

1.先用抓包软件fiddler或charles将请求抓到，然后导出为har文件，放到data文件夹

2.进入data文件夹，执行命令[``` har2case 文件名.har -2y ```]

3.可以看到在data目录下生成了【文件名.yml】文件

4.进入test_List文件，添加

示例代码：
```python
class Test_List():

    @pytest.mark.datafile("data/文件名.yml")
    def test_eg(self, env, parameters, token):
        parameters_request(env, parameters, token)
        
```
---

- 执行脚本
```python
py.test
```
- 指定–alluredir选项及结果数据保存的目录
```
pytest --alluredir ./result/
```
- 测试数据生成测试报告页面
```
allure generate ./result/ -o ./report/ --clean
```

---

**相关错误**

---

>将获取测试数据的函数分离，在执行pytest调用测试主函数时，抛出错误，提示找不到相关模块
```
__________________________________________________________________________________________________ ERROR collecting tests/test_Login.py __________________________________________________________________________________________________
ImportError while importing test module 'E:\110_pytest\tests\test_Login.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
tests\test_Login.py:6: in <module>
    from utils.commlib import get_test_data
E   ModuleNotFoundError: No module named 'utils'
```

此时需要在导入模块前加入这两句,必须写在[from xxx.xxx import xxx]之前,否则无效
```
import os, sys, allure, requests
sys.path.append(os.getcwd())
```

---

**其他说明**

---


需要找到har2case包所在位置，修改core.py文件
```python
IGNORE_REQUEST_HEADERS中，加入自己需要过滤的头部属性
```

```python
teststep_dict = {
            "name": "",
            "request": {},
            "validate": []
        }

找到以上内容，修改为

teststep_dict = {
            "name": "",
            "request": {},
            "validate": {}
        }
```
>找到方法def _make_validate(self, teststep_dict, entry_json):

```python
以下代码
teststep_dict["validate"].append(
            {"eq": ["status_code", entry_json["response"].get("status")]}
        )

修改为

teststep_dict["validate"]["status"] = entry_json["response"].get("status")
```

```python
以下代码
teststep_dict["validate"].append(
                    {"eq": ["content.{}".format(key), value]}
                )

修改为

teststep_dict["validate"][format(key)] = value

```

```python
以下代码
teststep_dict["validate"].append(
                {"eq": ["headers.Content-Type", headers_mapping["Content-Type"]]}
            )

修改为

teststep_dict["validate"]["Content-Type"] = headers_mapping["Content-Type"]

```

```python
找到以下代码
        if method in ["POST", "PUT", "PATCH"]:
            postData = entry_json["request"].get("postData", {})
            mimeType = postData.get("mimeType")

            # Note that text and params fields are mutually exclusive.
            request_data_key = "data"
            if not mimeType:
                pass
            elif mimeType.startswith("application/json"):
                try:
                    post_data = json.loads(post_data)
                    request_data_key = "json"
                except JSONDecodeError:
                    pass
            elif mimeType.startswith("application/x-www-form-urlencoded"):
                post_data = utils.convert_x_www_form_urlencoded_to_dict(post_data)
            else:
                # TODO: make compatible with more mimeType
                pass
替换为
        if method in ["POST", "PUT", "PATCH", "GET"]:
            postData = entry_json["request"].get("postData", {})
            mimeType = postData.get("mimeType")

            # Note that text and params fields are mutually exclusive.
            if "text" in postData:
                post_data = postData.get("text")
            else:
                params = postData.get("params", [])
                post_data = utils.convert_list_to_dict(params)

            request_data_key = "data"
            if not mimeType:
                pass
            elif mimeType.startswith("application/json"):
                try:
                    post_data = json.loads(post_data)
                except JSONDecodeError:
                    pass
            elif mimeType.startswith("application/x-www-form-urlencoded"):
                post_data = utils.convert_x_www_form_urlencoded_to_dict(post_data)
            elif mimeType.startswith("text/plain"):
                try:
                    post_data = json.loads(post_data)
                except JSONDecodeError:
                    pass
            else:
                # TODO: make compatible with more mimeType
                pass
```

修改源码是方便使用自己习惯的断言，用dict获取字段值比较直接

另外是har文件转为yml文件时，加多一个判断，当文件格式为text/plain，将内容转换为json格式

