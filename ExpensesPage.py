# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import init_driver
import SetUpFile


class ExpensesPage(init_driver.InitDriver):

    url_path = "/accounting/expenses"
    title = "Списания"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Списания')]"
    exportExcelBtn = "//a[@href='/accounting/expenses/downloadFile']"
    expenseDate = ".//*[@id='item-list-container']/div[2]/div[1]"
    expenseDescription = ".//*[@id='item-list-container']/div[2]/div[2]"
    expenseAmount = ".//*[@id='item-list-container']/div[2]/div[3]"

    def go_to_action_expenses_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_expenses_page(self):
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

    def get_expense_date(self):
        print(inspect.stack()[0][3])
        date = self.wait_for_element(self.expenseDate).text
        return date
        pass

    def get_expense_description(self):
        print(inspect.stack()[0][3])
        description = self.wait_for_element(self.expenseDescription).text
        return description
        pass

    def get_expense_amount(self):
        print(inspect.stack()[0][3])
        amount = self.wait_for_element(self.expenseAmount).text
        return amount
        pass
