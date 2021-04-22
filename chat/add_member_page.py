from time import sleep

from selenium.webdriver.common.by import By

from chat.basepage import BaseTest


class AddMember(BaseTest):

    def add_member(self, name, number, phone_num):
        from chat.contact_page import ContactPage
        self.driver.implicitly_wait(10)
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(number)
        self.find(By.ID, "memberAdd_phone").send_keys(phone_num)
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")
        sleep(1)
        return ContactPage(self.driver)
