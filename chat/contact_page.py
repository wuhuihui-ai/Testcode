from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from chat.add_member_page import AddMember
from chat.basepage import BaseTest


class ContactPage(BaseTest):
    def click_add_menber(self):
        self.driver.implicitly_wait(10)
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显示等待，等待元素是可点击状态
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            self.find(*ele).click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMember(self.driver)

    def get_member(self):
        info = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        phone_list = []
        # for a in info:
        #     if a.get_attribute("title") == "15263526351":
        #         return True
        for a in info:
            phone_list.append(a.get_attribute("title"))
        return phone_list
