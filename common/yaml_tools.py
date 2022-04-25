import json

import yaml
from common import constant


class YamlTools:

    def __init__(self):
        pass

    def write_yaml(self, *args):
        """
        把自定义的类型数据写入yaml文件
        :param args:
        :param kwargs:
        :return:
        """
        with open(args[0], "w", encoding="utf-8") as file:
            yaml.dump(args[1], stream=file, allow_unicode=True)

    def write_yaml_all(self, *args):
        with open(args[0], "w", encoding="utf-8") as file:
            yaml.dump_all([args[1], args[2]], stream=file, allow_unicode=True)

    def read_yaml(self, file):
        """
        读取yaml的内容
        :param args:
        :return:
        """
        with open(file, "r", encoding="utf-8") as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def read_yaml_all(self, file):
        """
        读取yaml中的多条数据，并返回一个列表
        :param file: yaml文件
        :return:list
        """
        with open(file, "r", encoding="utf-8") as file:
            datas = yaml.load_all(file, Loader=yaml.FullLoader)
            return [data for data in datas]


if __name__ == '__main__':
    yt = YamlTools()
    obj1 = [{"build_value": "1栋1单元",
             "room_value": "1A"
             }]

    # obj2 = {'case_title': '扫码登记',
    #         'method': 'post',
    #         'url': '/checkins/qrcodes?lang=zh_MO',
    #         'headers': {"Authorization": "#token#", "Content-Type": "application/x-www-form-urlencoded"},
    #         'data': {"activityId": "#activity_id#", "qrcode": "#qrcode#"}}

    yt.write_yaml(constant.house_list_data_dir, obj1)
    # yt.write_yaml_all(constant.house_data_dir, obj1)
    obj = yt.read_yaml(constant.house_list_data_dir)
    # obj_list = yt.read_yaml_all(constant.activity_data_dir)
    # print(obj_list)
    print(json.dumps(obj))
