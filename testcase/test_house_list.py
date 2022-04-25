from testcase.__init__ import *


# @pytest.mark.test
@pytest.mark.usefixtures("login_driver")
class TestHouseList:
    datas = YamlTools().read_yaml(constant.house_list_data_dir)

    @pytest.mark.parametrize('data', datas)
    def test_room_search(self, login_driver, data):
        login_driver[1][3].mylog.info("执行二手房列表检索")
        Index(login_driver[0]).goto_sell_house_list()
        text = HouseList(login_driver[0]).get_house_room(data).check_build_text(data)
        try:
            assert text
            login_driver[1][3].mylog.info("列表房号检索成功")
        except AssertionError:
            login_driver[1][3].mylog.info("检索失败")
