from page_locater.__init__ import *


class HouseListPage:
    add_house_button = (MobileBy.ID, 'com.kfang.agent:id/add_house')  # 添加拓房按钮
    more_search = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector.text("更多(2)")')
    price_text = (MobileBy.XPATH,
                  '//android.view.ViewGroup[@resource-id="com.kfang.agent:id/item_root"][0]'
                  '//android.widget.TextView[@resource-id="com.kfang.agent:id/house_price" and @text="#6666#"]')

    #  房号检索框元素
    room_search = (MobileBy.ID, "com.kfang.agent:id/room_search")  # 房号搜索框定位
    build_input = (MobileBy.ID, 'com.kfang.agent:id/house_et_building_and_unit')
    room_input = (MobileBy.ID, 'com.kfang.agent:id/house_et_room')
    confirm_button = (MobileBy.ID, 'com.kfang.agent:id/house_btn_ok')

    # 列表数据元素
    text1 = (MobileBy.ID, 'com.kfang.agent:id/house_region_number_type')
