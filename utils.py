from selenium import webdriver

class DriverUtil:
    # 定义类属性保存驱动对象
    driver=None
    kaiguan=True

    # 获取浏览器驱动对象  类方法
    @classmethod
    def get_driver(cls):
        # 判断_driver中是否存有驱动,如果没有实例化一个保存在_driver中
        # 返回_driver中的驱动对象
        if cls.driver is None:
            cls.driver=webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(20)
        return cls.driver




    # 退出浏览器驱动对象 类方法
    @classmethod
    def quit_driver(cls):
        # 如果_driver属性中有驱动对象,退出驱动对象-重置为None
        if cls.kaiguan == True and cls.driver is not None:
            cls.driver.quit()
            cls.driver =None
