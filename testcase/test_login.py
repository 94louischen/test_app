from testcase.__init__ import *


@pytest.mark.test
@pytest.mark.usefixtures("get_driver")
class TestLogin:

    # @pytest.mark.parametrize # 传参
    @pytest.mark.flaky(reruns=3, reruns_delay=1)  # 增加失败重试次数每秒重试1次共3次
    def test_login(self, get_driver):
        get_driver[1][3].mylog.info("执行登录用例")
        Login(get_driver[0]).login(get_driver[1][0].get_value("data", "user"), get_driver[1][0].get_value("data", "pwd"))
        try:
            assert Index(get_driver[0]).check_message() is True
            get_driver[1].mylog.info("登录成功")
        except AssertionError:
            get_driver[1].mylog.info("登录失败")
