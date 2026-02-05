from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        return webdriver.Chrome()
