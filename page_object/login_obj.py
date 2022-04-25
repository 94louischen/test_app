from page_object.__init__ import *


class Login(BaseContext):
    lg = DoLogs(__name__)

    def login(self, user, pwd):
        """
        登录
        :param user:
        :param pwd:
        :return:
        """
        self.input_text(LoginPage.input_username_loc, user, img_doc="请输入用户名")
        self.input_text(LoginPage.input_password_loc, pwd, img_doc="请输入密码")
        self.click_element(LoginPage.submit_login_loc, "点击登录按钮")
        time.sleep(2)