from testcase.__init__ import *


# @pytest.mark.test
@pytest.mark.usefixtures("login_driver")
class TestAddHouse:
    datas = YamlTools().read_yaml(constant.house_add_data_dir)

    @pytest.mark.parametrize('data', datas)
    def test_add_house(self, login_driver, data):
        login_driver[1][3].mylog.info("执行添加拓房用例")
        Index(login_driver[0]).goto_add_house()
        AddHouse(login_driver[0]).add_house(data).toast_confirm()
        try:
            assert Index(login_driver[0]).check_message() == "处理成功"
            login_driver[1][3].mylog.info("拓房成功")
        except AssertionError:
            login_driver[1][3].mylog.info("拓房失败")
