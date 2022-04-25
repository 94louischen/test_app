from page_object.__init__ import *

log = DoLogs(__name__)


class HouseList(BaseContext):

    def check_price_text(self, args):
        """
        检查是否存在指定的价格文本
        :return:返回boole值
        """
        self.wait_element_visible(util_tools.update_content(args.get("price_value"), HouseListPage.price_text),
                                  "等待列表价格文本出现")
        text = self.get_text(util_tools.update_content(args.get("price_value"), HouseListPage.price_text),
                             "获取列表价格文本元素值")
        if text:
            result = True
        else:
            result = False
        return result

    def get_house_room(self, args):
        """
        房号检索
        :param args:
        :return:
        """
        self.click_element(HouseListPage.room_search, "展开房号输入框")
        self.input_text(HouseListPage.build_input, args.get("build_value"), img_doc="输入楼栋单元")
        self.input_text(HouseListPage.room_input, args.get("room_value"), img_doc="输入房号")
        self.click_element(HouseListPage.confirm_button, "点击确定按钮")
        return self

    def check_build_text(self, args):
        """
        检查是否存在指定的楼栋文本
        :param args:
        :return:
        """
        text = self.get_text(HouseListPage.text1, "获取指定楼栋文本值")
        if text:
            result = True
        else:
            result = False
        return result

    def goto_house_detail(self):
        """
        从房源列表进入详情页
        :return:
        """
        self.click_element(HouseListPage.text1, "点击指定文本元素")
