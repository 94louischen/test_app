from page_object.__init__ import *


class AddHouse(BaseContext):

    def add_house(self, args):
        """
        拓房
        :param args:接收一个字典其中包含所有的拓房需要的必填参数
        :return:
        """
        self.click_element(AddHousePage.sell_table, "选择售")
        self.click_element(AddHousePage.garden_select, "进入楼盘选择页面")
        self.input_text(AddHousePage.input_garden, args.get("garden_value"), img_doc="输入楼盘信息")
        self.click_element(util_tools.update_content(args.get("garden_value"), AddHousePage.garden_value), "点击指定的楼盘")
        self.click_element(AddHousePage.use_select, "展开用途列表")
        self.click_element(util_tools.update_content(args.get("use_value"), AddHousePage.use_value), "选择用途")
        self.click_element(AddHousePage.building_select, "展开楼栋列表")
        self.click_element(util_tools.update_content(args.get("building_value"), AddHousePage.building_value), "选择楼栋")
        self.click_element(util_tools.update_content(args.get("floor_value"), AddHousePage.floor_value), "选择楼层")
        self.click_element(util_tools.update_content(args.get("room_value"), AddHousePage.room_value), "选择房号")
        self.click_element(AddHousePage.decoration_select, "展开装修列表")
        self.click_element(AddHousePage.decoration_value, "选择普通装修")
        self.click_element(AddHousePage.sell_price_type_select, "展开售价类型")
        self.click_element(AddHousePage.price_type_value, "选择售价类型")
        self.input_text(AddHousePage.price_value, args.get("price_value"), img_doc="输入售价值")
        self.click_element(AddHousePage.owner_info, "展开业主信息列表")
        self.click_element(AddHousePage.add_owner_button, "点击新增业主按钮")
        self.input_text(AddHousePage.input_name, args.get("input_name"), img_doc="输入业主姓名")
        self.input_text(AddHousePage.input_phone, args.get("input_phone"), img_doc="输入业主电话")
        self.click_element(AddHousePage.owner_relation, "展开业主关系列表")
        self.click_element(AddHousePage.ownership_value, "选择业主类型")
        self.click_element(AddHousePage.select_switch, "设置主要联系人")
        self.click_element(AddHousePage.submit_button, "点击完成按钮")
        self.click_element(AddHousePage.back, "点击返回按钮")
        self.click_element(AddHousePage.confirm_button, "拓房确认")
        return self

    def toast_confirm(self):
        if self.wait_element_visible(AddHousePage.toast_confirm, "等待是否有提示框", timeout=1):
            self.click_element(AddHousePage.toast_confirm, "点击“好的”按钮")
