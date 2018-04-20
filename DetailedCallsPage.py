# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class DetailedCallsPage(init_driver.InitDriver):

    url_path = "/accounting/callDetails"
    title = "Детализация вызовов"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Детализация вызовов')]"
    exportExcelBtn = "//*[text()='Экспорт в Excel']"
    calldateLocator = "//*[@id='item-list-container']/div[2]/div[1]"
    callcommentLocator = "//*[@id='item-list-container']/div[2]/div[2]"
    fromNumberLocator = "//*[@id='item-list-container']/div[2]/div[3]"
    toNumberLocator = "//*[@id='item-list-container']/div[2]/div[4]"
    amountLocator = "//*[@id='item-list-container']/div[2]/div[5]"
    durationLocator = "//*[@id='item-list-container']/div[2]/div[6]"

    def go_to_detailed_calls_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_detailed_calls_page(self):
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

    def export_excel(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.exportExcelBtn).click()
        pass

    def get_call_date(self):
        print(inspect.stack()[0][3])
        call_date = self.wait_for_element(self.calldateLocator).text
        return call_date
        pass

    def get_call_comment(self):
        print(inspect.stack()[0][3])
        call_comment = self.wait_for_element(self.callcommentLocator).text
        return call_comment
        pass

    def get_call_from_number(self):
        print(inspect.stack()[0][3])
        from_number = self.wait_for_element(self.fromNumberLocator).text
        return from_number
        pass

    def get_call_to_number(self):
        print(inspect.stack()[0][3])
        to_number = self.wait_for_element(self.toNumberLocator).text
        return to_number
        pass

    def get_call_amount(self):
        print(inspect.stack()[0][3])
        amount = self.wait_for_element(self.amountLocator).text
        return amount
        pass

    def get_call_duration(self):
        print(inspect.stack()[0][3])
        duration = self.wait_for_element(self.durationLocator).text
        return duration
        pass
