import time
import unittest

from report.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from script.cart_case import TestCart
from script.login_case import TestLogin
from utils import DriverUtil

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
DriverUtil.kaiguan = False
with open("./report/report.html", "wb") as f:
    runner = HTMLTestRunner(stream=f, title="tpshop商城测试用例", description="报告描述")
    runner.run(suite)


DriverUtil.kaiguan = True
DriverUtil.quit_driver()
