# 测试套件
import unittest

# 添加用例
from script.cart_case import TestCart
from script.login_case import TestLogin
from utils import DriverUtil


suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))


DriverUtil.kaiguan =False

# 创建运行器
runner=unittest.TextTestRunner()
runner.run(suite)
# 运行
DriverUtil.kaiguan = True
DriverUtil.quit_driver()


