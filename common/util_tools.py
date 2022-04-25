import re
import uuid
import hashlib
import random
import datetime
import configparser
from common.ConfTools import DoConf
from common import constant
from common.LogTools import DoLogs

log = DoLogs(__name__)


class Context:
    token = None  # 验票员
    activity_title = None  # 活动标题
    activity_id = None  # 活动id
    qrcode = None  # 活动二维码


def param_replace(data):
    """
    替换data中带##的字段
    :param data:
    :return:
    """
    if data:
        p = "#(.*?)#"
        if type(data) != str:
            data = str(data)
        while re.search(p, data):
            params = re.search(p, data)
            params1 = params.group(1)
            try:
                params2 = DoConf(constant.globe_conf_dir).get_value('data', params1)
                if type(params2) != str:
                    params2 = str(params2)
            except configparser.NoOptionError as e:
                if hasattr(Context, params1):
                    params2 = getattr(Context, params1)
                    if type(params2) != str:
                        params2 = str(params2)
                else:
                    print("找不到相关值")
                    raise e
            data = re.sub(p, params2, data, count=1)
    return eval(data)


def get_random_number(data=None):
    """
    生成一个当前日期和随机数的组合
    :param data:
    :return:
    """
    if data:
        today = datetime.datetime.now().strftime('%m%d')
        num = random.randint(1, 100)
        data = data + "_" + today + str(num)
        return data


def modify_date(data):
    if data:
        if not (isinstance(data, str)):
            data = str(data)
        # 匹配2020-07-06T19:00:00这样的日期，然后取T后面的值
        p = "A\\d{4}-\\d{2}-\\d{2}(T\\d{2}:\\d{2}:\\d{2})A"
        p1 = "B(\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2})B"
        while re.search(p, data):
            params1 = re.search(p, data).group(1)
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            update_time = today + params1
            # 替换所传参数中的日期
            data = re.sub(p, update_time, data, count=1)
        # 匹配以"B()B"包裹的日期字段，并替换为当前日期
        if re.search(p1, data):
            today = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%Y-%m-%dT%H:%M:%S')
            data = re.sub(p1, today, data, count=1)
    return data


# 针对get请求的query参数加密
def get_md5(data):
    str1 = ''
    data["nonce"] = str(uuid.uuid4())
    keys = list(data.keys())
    keys.sort()
    for i in keys:
        str1 += i + '=' + data[i]
    signature_value = str1 + 'activity'
    log.mylog.info(f"signature_value的值为:{signature_value}")
    signature_value_md5 = hashlib.md5(signature_value.encode(encoding='UTF-8')).hexdigest()
    log.mylog.info(f"signature_value的值为:{signature_value_md5}")
    data['signature'] = signature_value_md5
    return data


# 针对post请求query部分与body部分参数进行md5加密
def post_md5(url, data):
    dict1 = {}
    str1 = ''
    nonce_value = str(uuid.uuid4())
    url = url + '&' + 'nonce' + '=' + nonce_value
    query = url.split("?")[1].split("&")
    for i in query:
        a, b = i.split("=")
        dict1[a] = b
    if data:
        if type(data) == str:
            data = eval(data)
        dict1.update(data)
    keys = list(dict1.keys())
    keys.sort()
    for i in keys:
        if isinstance(dict1[i], list) or isinstance(dict1[i], int) or isinstance(dict1[i], dict):
            dict1[i] = str(dict1[i])
            dict1[i] = dict1[i].replace(' ', '').replace('\'', '\"')
        str1 += i + '=' + dict1[i]
    signature_value = str1 + 'activity'
    log.mylog.info(f"signature_value的值为:{signature_value}")
    signature_value_md5 = hashlib.md5(signature_value.encode(encoding='UTF-8')).hexdigest()
    log.mylog.info(f"signature_value的值为:{signature_value_md5}")
    new_url = url + '&' + 'signature' + '=' + signature_value_md5
    return new_url


def update_content(param, loc):
    """
    替换元素定位中的固定文本
    :param param:需要替换的文本
    :param loc:原字符串
    :return:返回新的元素定位
    """
    import re
    # p = u"[\u4e00-\u9fa5]+"
    p = '#(.*?)#'
    new_loc = eval(re.sub(p, param, str(loc), count=1))
    return new_loc


if __name__ == '__main__':
    data = {'lang': 'zh_MO'}
    print(get_md5(data))
