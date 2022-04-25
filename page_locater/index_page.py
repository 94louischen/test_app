from page_locater.__init__ import *


class IndexPage:
    homepage_fixed_text = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("角色房源")')  # 首页固定文本
    sell_icon = (
    MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.kfang.agent:id/tv_city_menu").text("二手房")')  # 二手房图标
    rent_icon = (MobileBy.ID, 'com.kfang.agent:id/home_iv_sell')  # 租房图标
    new_house_icon = (MobileBy.ID, 'com.kfang.agent:id/home_iv_sell')  # 新房图标
    booth = (MobileBy.ID, 'com.kfang.agent:id/home_iv_sell')  # 展位图标
    add_owner_icon = (MobileBy.ID, 'com.kfang.agent:id/home_iv_sell')  # 录客图标

    add_house_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("拓房")')  # 添加拓房图标
    maintain_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("抢维护")')
    key_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("做钥匙人")')
    survey_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("做实勘人")')
    entrusted_icon = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("做委托人")')

    text1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiuSelector().text("角色房源")')

    success_toast = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("处理成功")')
