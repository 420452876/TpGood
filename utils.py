from selenium import webdriver

class UtilsDriver :
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None :
            # 获取浏览器驱动对象
            cls._driver = webdriver.Chrome()
            # 窗口最大化
            cls._driver.maximize_window()
            # 设置隐试时间
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None :
            cls.get_driver().quit()
            cls._driver = None


