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

- 执行所有符合命名规范的文件
```python
py.test -v
```
- 指定环境执行特定文件
```python
py.test tests/test_List.py -v --env test/110/prod #(可选，pytest_addoption中可查看，默认为110)
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

