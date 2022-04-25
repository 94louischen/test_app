from page_locater.__init__ import *


class AuthPage:
    allow_button = (MobileBy.ID, 'com.kfang.agent:id/app_btn_location')  # 允许按钮
    tips_allow_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelecor().text("允许")')  # 提示框允许按钮
    back_button = (MobileBy.ACCESSIBILITY_ID, '转到上一层级')  # 左上角 >返回上一层按钮

