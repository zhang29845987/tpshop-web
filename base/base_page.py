# 对象库层基类
from selenium.webdriver.common.by import By

from utils import DriverUtil


class BasePage:
    # 在初始化方法中获取到浏览器驱动对象保存到driver
    def __init__(self):
        self.driver=DriverUtil.get_driver()

    # 封装元素定位方法,参数-(定位方法 定位依据)
    def base_find_element(self,elemint):
        # find_element定位元素-- 传入两个参数-定位方法-定位依据
        return self.driver.find_element(elemint[0],elemint[1])


# 操作层基类
class BaseHandle:
    # 封装元素输入文本操作 参数-输入元素和输入文本
    def base_input(self,element,text):
        element.clear()
        element.send_keys(text)

    def base_click(self,element):
        element.click()


