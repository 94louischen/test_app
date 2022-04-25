from page_locater.__init__ import *


class LoginPage:
    """
    登录页面
    """
    input_username_loc = (MobileBy.ID, "com.kfang.agent:id/et_username")  # 用户名输入框控件
    input_password_loc = (MobileBy.ID, "com.kfang.agent:id/et_password")  # 密码输入框控件
    submit_login_loc = (MobileBy.ID, "com.kfang.agent:id/btn_login")  # 登录提交按钮
