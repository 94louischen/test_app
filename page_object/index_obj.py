from page_object.__init__ import *


class Index(BaseContext):

    def check_message(self):
        """
        获取成功提示的文本
        :return:
        """
        self.wait_element_presence(IndexPage.success_toast, "等待成功提示出现")
        text = self.get_text(IndexPage.success_toast, "获取成功提示文本")
        return text

    def goto_add_house(self):
        self.click_element(IndexPage.add_house_icon, "在首页点击“拓房”icon")
        return self

    def goto_sell_house_list(self):
        self.click_element(IndexPage.sell_icon, "进入二手房列表")
