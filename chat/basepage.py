from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class BaseTest:
    base_url = ""

    def __init__(self, base_driver: webdriver = None):
        if base_driver is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
        else:
            self.driver = base_driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        ele: WebElement = self.find(by, locator)
        ele.click()
        return ele

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
