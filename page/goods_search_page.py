from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class GoodsSearchPage(BasePage):
    # init方法
    def __init__(self):
        super().__init__()
        # 调用父类init方法,实例化浏览器驱动对象
        # 页面元素定位信息
        self.spxqing=(By.XPATH,'//div[@class="shop_name2"]/a[contains(text(),"{}")]')


    # 定位商品名超链接 -- 参数--商品名关键字
    def find_goods_item(self,name):
        ss=(self.spxqing[0],self.spxqing[1].format(name))
        return self.base_find_element(ss)


# 操作层
class GoodsSearchHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.searchpage=GoodsSearchPage()

    # 点击商品名超链接--参数-商品名关键字
    def click_goods_name(self,name):
        self.base_click(self.searchpage.find_goods_item(name))


# 业务层
class GoodsSearchProxy:

    # init方法
    def __init__(self):
        # 获取操作层对象
        self.searchhandle=GoodsSearchHandle()

    # 进入指定商品详情页--参数-商品名关键字
    def to_goods_detail_page(self,name):
        # 点击指定商品
        self.searchhandle.click_goods_name(name)
