from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from selenium import webdriver

# 对象库层
from utils import DriverUtil


class LoginPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 调用父类init方法,实例化浏览器驱动对象
        # 页面元素定位信息
        self.username=(By.ID,"username")
        self.password=(By.ID,"password")
        self.verify_code=(By.ID,"verify_code")
        self.sbtbutton=(By.NAME,"sbtbutton")

    # 定位用户名输入框
    def find_username(self):
        return self.base_find_element(self.username)

    # 定位密码输入框
    def find_pwd(self):
        return self.base_find_element(self.password)

    # 定位验证码输入框
    def find_verify_code(self):
        return self.base_find_element(self.verify_code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.base_find_element(self.sbtbutton)


# 操作层
class LoginHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=LoginPage()

    # 输入用户名--参数-用户名
    def input_username(self,text1):
        self.base_input(self.page.find_username(),text1)

    # 输入密码--参数-密码
    def input_password(self,text):
        self.base_input(self.page.find_pwd(),text)

    # 输入验证码--参数-验证码
    def input_verify_code(self,text):
        self.base_input(self.page.find_verify_code(), text)

    # 点击登录按钮
    def click_login_btn(self):
        self.base_click(self.page.find_login_btn())


# 业务层
class LoginProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.loginhandle=LoginHandle()

    # 登录业务
    def login(self,text,text1,text2):
        # 输入用户名
        # 输入密码
        # 输入验证码
        # 点击登录
        self.loginhandle.input_username(text)
        self.loginhandle.input_password(text1)
        self.loginhandle.input_verify_code(text2)
        self.loginhandle.click_login_btn()



if __name__ == '__main__':
    driver=DriverUtil.get_driver()
    driver.get("http://127.0.0.1/Home/user/login.html")
#     # cc=LoginProxy()
#     # cc.login("18246640990","123456","8888")
#     # cc=LoginPage()
#     # cc.find_username().send_keys("18246640990")
#     # cc.find_pwd().send_keys("18246640990")
#     # cc.find_verify_code().send_keys("8888")
#     # cc.find_login_btn().click()
    cc=LoginProxy()
    cc.login("18246640990","123456","123456")













