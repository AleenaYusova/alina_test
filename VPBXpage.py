# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import init_driver
import SetUpFile


class VpbxPage(init_driver.InitDriver):

    url_path = "/services/vpbx"
    title = "Виртуальная АТС"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Виртуальная АТС')]"
    total_fee_amount = ".//*[@id='vpbx-main']//td[contains(.,'Всего абонентская плата')]/parent::*//b"

    def go_to_action_history_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_action_history_page(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path + self.url_path)
            pass

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            self.wait_for_element(self.navigationBarElement).click()
            time.sleep(3)
            assert self.driver.title in self.title
            pass

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()
        pass

    def get_total_fee_amount(self):
        fee = self.wait_for_element(self.total_fee_amount).text
        fee = fee.replace(' ', '')
        return fee
        pass
