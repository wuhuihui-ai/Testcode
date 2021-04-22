from time import sleep

import pytest
import yaml
from selenium.webdriver.support.wait import WebDriverWait

from chat.first_page import FirstPage


def data():
    with open("./data1.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas


def test():
    print(data()['testdata1'])


class TestCase:
    def setup(self):
        self.firstpage = FirstPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name, number, phone_num", data()['testdata1'],
                             ids=["data1"])
    def test_case(self, name, number, phone_num):
        ele1 = self.firstpage.first_page().click_add_menber().add_member(name, number, phone_num).get_member()
        sleep(2)
        assert phone_num in ele1

    @pytest.mark.parametrize("name, number, phone_num", data()['testdata2'],
                             ids=["data2"])
    def test_case2(self, name, number, phone_num):
        ele2 = self.firstpage.first_add_member().add_member(name, number, phone_num).get_member()
        sleep(2)
        assert phone_num in ele2
