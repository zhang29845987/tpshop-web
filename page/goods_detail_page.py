from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class GoodsDetailPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 调用父类init方法,实例化浏览器驱动对象
        # 业务元素定位信息
        self.jiaru=(By.ID,"join_cart")
        self.jieguo=(By.CSS_SELECTOR,".conect-title>span")

    # 定位加入购物车超链接
    def find_join_cart(self):
        return self.base_find_element(self.jiaru)

    # 定位加入结果提示信息
    def find_join_result(self):
        return self.base_find_element(self.jieguo)


# 操作层
class GoodsDetailHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.goods=GoodsDetailPage()

    # 点击加入购物车超链接
    def click_join_cart(self):
        self.base_click(self.goods.find_join_cart())

    # 获取加入结果提示信息文本--返回文本信息
    def get_join_result(self):
        return self.goods.find_join_result()



# 业务层
class GoodsDetailProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.goodhandle=GoodsDetailHandle()

    # 添加商品到购物车
    def join_goods_to_cart(self):
        self.goodhandle.click_join_cart()

    # 获取返回提示信息 -- 返回是否成功布尔值
    def get_join_result(self):
        return self.goodhandle.get_join_result().text

