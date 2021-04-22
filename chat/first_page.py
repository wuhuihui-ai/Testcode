from selenium.webdriver.common.by import By

from chat.add_member_page import AddMember
from chat.basepage import BaseTest
from chat.contact_page import ContactPage


class FirstPage(BaseTest):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def first_page(self):
        self.driver.implicitly_wait(10)
        self.find_and_click(By.ID, "menu_contacts")
        return ContactPage(self.driver)

    def first_add_member(self):
        self.driver.implicitly_wait(10)
        self.find_and_click(By.CSS_SELECTOR,".index_service_cnt_item_title")
        return AddMember(self.driver)
