from page_locater.__init__ import *


class HouseDetailPage:
    sell_entrust_tag = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector.text("出售委托")')
    rent_entrust_tag = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector.text("出租委托")')
    maintain_entrust_tag = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector.text("维护信息")')
    key_entrust_tag = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector.text("钥匙信息")')
    entrust_add_button = (MobileBy.ID, 'com.kfang.agent:id/house_sbtn_entrust_add')  # 添加委托按钮
    # 认证房源编码

    # 房源出售委托书
    # 产权证明
    # 身份证明