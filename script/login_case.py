# 创建测试类
import json
import time
import unittest
from parameterized import parameterized

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil

def data():
    cs=[]
    with open(BASE_DIR+"/data/shuju.json","r",encoding="utf8") as f:
        data1=json.load(f)
        for csd in data1:
            a=csd.get("a")
            b=csd.get("b")
            c=csd.get("c")
            d=csd.get("d")
            cs.append((a,b,c,d))
    print(cs)
    return cs

# 测试类
class TestLogin(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        cls.indexprxy=IndexProxy()
        cls.prxy=LoginProxy()
        cls.driver.get("http://localhost/")



    # def setUp(self):
    #     # 打开首页


    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 测试方法,断言
    @parameterized.expand(data)
    def test01_login(self,a,b,c,d):
        self.indexprxy.to_login_page()
        self.prxy.login(a,b,c)
        time.sleep(5)
        msg=self.driver.title
        print(msg)
        self.assertIn(d,msg)



# 参数化,数据驱动
