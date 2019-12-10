# 参数化,数据驱动
# 创建测试类
import json
import time
import unittest

from parameterized import parameterized

from config import BASE_DIR
from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil

def cart():
    ss=[]
    with open(BASE_DIR+"/data/cart.json","r",encoding="utf8") as f:
        cs=json.load(f)
        for aa in cs:
            a=aa.get("a")
            b=aa.get("b")
            c=aa.get("c")
            ss.append((a,b,c))
    print(ss)
    return ss


class TestCart(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        cls.indexproxy=IndexProxy()
        cls.goodssearchproxy=GoodsSearchProxy()
        cls.proxy=GoodsDetailProxy()
        cls.driver.get("http://localhost")


        # 打开首页


    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 创建测试方法,断言
    @parameterized.expand(cart)
    def test01_cart(self,keys,keys1,keys2):
        self.indexproxy.search_goods(keys)
        self.goodssearchproxy.to_goods_detail_page(keys1)
        self.proxy.join_goods_to_cart()
        time.sleep(5)
        ss=self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(ss)
        cs=self.proxy.get_join_result()
        self.assertIn(keys2,cs)



# 参数化,数据驱动
