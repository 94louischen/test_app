import requests
from common.LogTools import DoLogs


class Request:
    log = DoLogs(__name__)

    def __init__(self):
        self.session = requests.sessions.session()

    def http_request(self, method, url, data=None, json=None, headers=None, cookies=None):
        global resp
        self.log.mylog.debug("测试地址是{}".format(url))
        if json is None:
            self.log.mylog.debug("测试参数是{}".format(data))
        else:
            self.log.mylog.debug("测试参数是{}".format(json))
        if type(data) == str:
            data = eval(data)
        if type(json) == str:
            json = eval(json)
        if type(headers) == str:
            headers = eval(headers)
        method = method.upper()
        if method == "GET":
            resp = self.session.request(method, url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            if json:
                resp = self.session.request(method, url, json=json, headers=headers, cookies=cookies)
            else:
                resp = self.session.request(method, url, data=data, headers=headers, cookies=cookies)
        else:
            print("暂时不支持的格式")
        self.log.mylog.debug("响应信息是{}".format(resp.text))
        return resp

    def close(self):
        self.session.close()


if __name__ == '__main__':
    res = Request()
    url = 'http://wmoaapi.doocom.net/api/v1/users/auth/'
    params1 = {"deviceToken": "123456", "deviceId": "123456", "clientId": "123456", "username": "chtang",
               "password": "123456"}
    headers1 = '{"Content-Type": "application/x-www-form-urlencoded"}'
    test = res.http_request("post", url, params1, headers=headers1)
    print(type(test), test.text)
