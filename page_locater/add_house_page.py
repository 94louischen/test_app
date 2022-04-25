from page_locater.__init__ import *


class AddHousePage:
    sell_table = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("出售")')
    rent_table = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("出租")')
    rent_sell_table = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("租售")')
    data_table = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("资料")')

    garden_select = (MobileBy.ID, 'com.kfang.agent:id/tv_houses')  # 选择楼盘
    input_garden = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请输入楼盘名称")')
    garden_value = (
        MobileBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.kfang.agent:id/house_tv_garden").text("#陈旋的测试楼盘#")')

    use_select = (MobileBy.ID, 'com.kfang.agent:id/tv_use')  # 选择用途
    use_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("#普通住宅#")')

    building_select = (MobileBy.ID, 'com.kfang.agent:id/tv_repose')  # 选择坐落
    # building_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("#9栋9单元#").instance(0))')
    # building_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("#1栋1单元#")')
    building_value = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().resourceId("com.kfang.agent:id/repose_rv")).scrollTextIntoView("#9栋9单元#")')
    floor_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("#1层#")')
    room_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("#1A#")')

    unit_type_select = (MobileBy.ID, 'com.kfang.agent:id/tv_unit')  # 选择户型

    decoration_select = (MobileBy.ID, 'com.kfang.agent:id/tv_decoration')  # 选择装修
    decoration_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("普通装修")')

    orientation_select = (MobileBy.ID, 'com.kfang.agent:id/tv_orientation')  # 选择朝向

    area_select = (MobileBy.ID, 'com.kfang.agent:id/edt_area')  # 选择面积

    sell_price_type_select = (MobileBy.ID, 'com.kfang.agent:id/tv_sell_type')  # 选择售价类型
    price_type_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("实收")')

    price_value = (MobileBy.ID, 'com.kfang.agent:id/edit_sell_price')  # 价格值

    owner_info = (MobileBy.ID, 'com.kfang.agent:id/tv_owner')  # 选择业主信息
    add_owner_button = (MobileBy.ID, 'com.kfang.agent:id/btn_add_owner')  # 新增业主按钮
    input_name = (MobileBy.XPATH,
                  '//android.widget.TextView[@text="业主姓名"]/parent::android.widget.LinearLayout/following-sibling::android.widget.EditText[@resource-id="com.kfang.agent:id/sRightEditTextId"]')
    input_phone = (MobileBy.XPATH,
                   '//android.widget.TextView[@text="+86"]/parent::android.widget.LinearLayout/preceding-sibling::android.widget.EditText[@resource-id="com.kfang.agent:id/sRightEditTextId"]')
    owner_relation = (MobileBy.ID, 'com.kfang.agent:id/super_owner_relation')
    ownership_value = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("产权人")')
    select_switch = (MobileBy.ID, 'com.kfang.agent:id/sRightSwitchId')
    submit_button = (MobileBy.ID, 'com.kfang.agent:id/btn_commit')
    back = (MobileBy.ID, 'com.kfang.agent:id/btn_back')
    confirm_button = (MobileBy.ID, 'com.kfang.agent:id/btn_confirm')

    toast_confirm = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("好的")')  # 确认提示框“好的”按钮
