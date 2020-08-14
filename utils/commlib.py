import base64
import json
import random
import string
import time

import requests
import yaml
from Crypto.Cipher import AES


def get_test_data(*args):
    case = []
    http = []
    expected = []
    for arg in args:
        with open(arg, encoding='utf-8') as f:
            dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
            test = dat['teststeps']
            for td in test:
                case.append(td.get('name', ''))
                http.append(td.get('request', {}))
                expected.append(td.get('validate', {}))
        parameters = zip(case, http, expected)
    return case, parameters


def get_request(env, name, http, token):
    headers = http["headers"]
    headers["Authorization"] = token
    headers["Timestamp"] = str(round(time.time()) * 1000)
    requests.adapters.DEFAULT_RETRIES = 5
    r = requests.session()
    r.keep_alive = False
    r = requests.request(http["method"], url=env["data"]["url"] + name, headers=headers, json=http["data"])
    return r


def decode(key, data):
    cipher = AES.new(key)
    result2 = base64.b64decode(data)
    response = cipher.decrypt(result2)
    response = response.decode('utf-8', 'ignore')
    response = response.rstrip('\x01'). \
        rstrip('\x02').rstrip('\x03').rstrip('\x04'). \
        rstrip('\x05').rstrip('\x06').rstrip('\x07'). \
        rstrip('\x08').rstrip('\x09').rstrip('\x10'). \
        rstrip('\x0A').rstrip('\x0B').rstrip('\x0C'). \
        rstrip('\x0D').rstrip('\x0E').rstrip('\x0F'). \
        rstrip('\n').rstrip('\t').rstrip('\r')
    return response


def res_validate(data, validate, status_code):
    if "randomId" in data:
        response = decode(data["randomId"], data["encryptData"])
        res = json.loads(response)
        assert res["code"] == validate["code"]
        assert res["msg"] == validate["msg"]
        assert status_code == validate["status"]
    else:
        res = data
        assert res["code"] == validate["code"]
        assert res["msg"] == validate["msg"]
        assert status_code == validate["status"]


class Publice(object):
    def ranstr(self, num):
        salt = ''.join(random.sample(string.ascii_uppercase + string.digits, num))
        return salt

    def ranlong(self, num):
        salt = ''.join(random.sample(string.digits, num))
        return salt

    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def provinceNORandom(self):
        data = {
            '北京': ['北京'],
            '上海': ['上海'],
            '深圳': ['深圳'],
            '天津': ['天津'],
            '重庆': ['重庆'],
            '澳门': ['澳门'],
            '香港': ['香港'],
            '海南': ['海口', '三亚'],
            '台湾': ['台湾', '台北', '高雄', '基隆', '台中', '台南', '新竹', '嘉义'],
            '河北': ['唐山', '邯郸', '邢台', '保定', '承德', '沧州', '廊坊', '衡水', '石家庄', '秦皇岛', '张家口'],
            '山西': ['太原', '大同', '阳泉', '长治', '晋城', '朔州', '晋中', '运城', '忻州', '临汾', '吕梁'],
            '山东': ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城', '滨州', '荷泽',
                   '菏泽'],
            '江苏': ['南京', '无锡', '徐州', '常州', '苏州', '南通', '淮安', '盐城', '扬州', '镇江', '泰州', '宿迁', '连云港'],
            '浙江': ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水'],
            '安徽': ['合肥', '芜湖', '蚌埠', '淮南', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '巢湖', '六安', '亳州', '池州', '宣城',
                   '马鞍山'],
            '福建': ['福州', '厦门', '莆田', '三明', '泉州', '漳州', '南平', '龙岩', '宁德'],
            '江西': ['南昌', '萍乡', '新余', '九江', '鹰潭', '赣州', '吉安', '宜春', '抚州', '上饶', '景德镇'],
            '河南': ['郑州', '开封', '洛阳', '焦作', '鹤壁', '新乡', '安阳', '濮阳', '许昌', '漯河', '南阳', '商丘', '信阳', '周口', '驻马店', '济源',
                   '平顶山', '三门峡'],
            '湖北': ['武汉', '黄石', '襄樊', '十堰', '荆州', '宜昌', '荆门', '鄂州', '孝感', '黄冈', '咸宁', '随州', '恩施', '仙桃', '天门', '潜江'],
            '湖南': ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '益阳', '郴州', '永州', '怀化', '娄底', '吉首', '张家界'],
            '广东': ['广州', '深圳', '珠海', '汕头', '韶关', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源', '阳江', '清远', '东莞',
                   '中山', '潮州', '揭阳', '云浮'],
            '广西': ['南宁', '柳州', '桂林', '梧州', '北海', '钦州', '贵港', '玉林', '百色', '贺州', '河池', '来宾', '崇左', '防城港'],
            '四川': ['成都', '自贡', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '宜宾', '广安', '达州', '眉山', '雅安', '巴中', '资阳',
                   '西昌', '攀枝花'],
            '贵州': ['贵阳', '遵义', '安顺', '铜仁', '毕节', '兴义', '凯里', '都匀', '六盘水', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州'],
            '云南': ['昆明', '曲靖', '玉溪', '保山', '昭通', '丽江', '思茅', '临沧', '景洪', '楚雄', '大理', '潞西'],
            '陕西': ['西安', '铜川', '宝鸡', '咸阳', '渭南', '延安', '汉中', '榆林', '安康', '商洛'],
            '甘肃': ['兰州', '金昌', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南', '临夏', '合作', '嘉峪关'],
            '辽宁': ['沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '盘锦', '阜新', '辽阳', '铁岭', '朝阳', '葫芦岛'],
            '吉林': ['长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城', '延吉'],
            '黑龙江': ['鹤岗', '鸡西', '大庆', '伊春', '黑河', '绥化', '双鸭山', '牡丹江', '佳木斯', '七台河''哈尔滨', '齐齐哈尔', ],
            '青海': ['西宁', '德令哈', '格尔木'],
            '宁夏': ['银川', '吴忠', '固原', '中卫', '石嘴山'],
            '西藏': ['拉萨', '日喀则'],
            '新疆': ['哈密', '和田', '喀什', '昌吉', '博乐', '伊宁', '塔城', '吐鲁番', '阿图什', '库尔勒', '五家渠', '阿克苏', '阿勒泰', '石河子', '阿拉尔',
                   '乌鲁木齐', '克拉玛依', '图木舒克'],
            '内蒙古': ['包头', '乌海', '赤峰', '通辽', '鄂尔多斯', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '兴安盟', '呼和浩特', '锡林郭勒盟', '阿拉善盟', '巴彦淖尔盟',
                    '乌兰察布盟'],
        }
        provincelist = list(data.keys())
        province = random.choice(provincelist)
        city = random.choice(data[province])
        return {
            "province": province,
            "city": city
        }
