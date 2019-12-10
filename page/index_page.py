from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
from utils import DriverUtil


class IndexPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 调用父类init方法,实例化浏览器驱动对象
        # 页面元素定位信息
        self.denglu=(By.LINK_TEXT,"登录")
        self.shuru=(By.ID,"q")
        self.sousuo=(By.CLASS_NAME,"ecsc-search-button")

    # 定位登录超链接
    def find_login_link(self):
       return self.base_find_element(self.denglu)

    # 定位搜索输入框
    def find_search_input(self):
        return self.base_find_element(self.shuru)

    # 定位搜索按钮
    def find_search_btn(self):
        return self.base_find_element(self.sousuo)


# 操作层
class IndexHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=IndexPage()

    # 点击登录超链接
    def click_login_link(self):
        self.base_click(self.page.find_login_link())

    # 输入框搜索 -- 参数-搜索关键字
    def input_search_text(self,text):
        self.base_input(self.page.find_search_input(),text)


    # 点击搜索按钮
    def click_search_btn(self):
        self.base_click(self.page.find_search_btn())


# 业务层
class IndexProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=IndexHandle()

    # 点击登录前往登录页
    def to_login_page(self):
        # 点击登录超链接
        self.handle.click_login_link()

    # 搜索商品
    def search_goods(self, name):

        # 输入关键字
        # 点击搜索按钮
        self.handle.input_search_text(name)
        self.handle.click_search_btn()

if __name__ == '__main__':
    ss=DriverUtil.get_driver()
    ss.get("http://127.0.0.1")
    aa=IndexProxy()
    aa.search_goods("小米")