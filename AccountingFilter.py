# -*- coding: utf-8 -*-
#
import datetime
import inspect
import unittest
import sys
from selenium.webdriver.common.keys import Keys
import init_driver


class AccountingFilter(init_driver.InitDriver):

    documentFilter_doctype = "//*[@id='DocumentFilter_doctype-styler']"
    allDocumentsSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Все документы')]"
    contractSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Договор')]"
    applicationSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Заявление')]"
    appendixSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Приложение')]"
    agreementSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Соглашение')]"
    accountingDocumentsSelect = "//*[@id='DocumentFilter_doctype-styler']//ul/li[contains(.,'Бухгалтерские документы')]"
    dateFromField = ".//*[@id='DocumentFilter_startPeriod']"
    dateToField = ".//*[@id='DocumentFilter_endPeriod']"

    def search_all_types(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.allDocumentsSelect).click()
        pass

    def search_contract_type(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.contractSelect).click()
        pass

    def search_application_type(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.applicationSelect).click()
        pass

    def search_appendix_type(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.appendixSelect).click()
        pass

    def search_agreement_type(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.agreementSelect).click()
        pass

    def search_accounting_documents_type(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.documentFilter_doctype).click()
        self.wait_for_element(self.accountingDocumentsSelect).click()
        pass

    def set_date_from(self, number_ofdays_tosubtracts_from_today=0):
        print(inspect.stack()[0][3])

        # очищается поле
        self.wait_for_element(self.dateFromField).clear()

        # генириться текущая дата
        today = datetime.date.today()

        # от текущей даты отнимается переданное в функцию кол-во дней
        date_to_set = today - datetime.timedelta(days=number_ofdays_tosubtracts_from_today)

        # изменяется формат на день, месяц, год
        date_to_set = date_to_set.strftime("%d.%m.%Y")

        # вводиться дата и нажимается Enter
        self.wait_for_element(self.dateFromField).send_keys(date_to_set)
        self.wait_for_element(self.dateFromField).send_keys(Keys.ENTER)

        # делается клик в любое место на странице, что бы скрыть календарь
        self.wait_for_element("html/body").click()
        pass

    def set_date_to(self, number_ofdays_tosubtracts_from_today=0):
        print(inspect.stack()[0][3])

        # очищается поле
        self.wait_for_element(self.dateToField).clear()

        # генириться текущая дата
        today = datetime.date.today()

        # от текущей даты отнимается переданное в функцию кол-во дней
        date_to_set = today - datetime.timedelta(days=number_ofdays_tosubtracts_from_today)

        # изменяется формат на день, месяц, год
        date_to_set = date_to_set.strftime("%d.%m.%Y")

        # вводиться дата и нажимается Enter
        self.wait_for_element(self.dateToField).send_keys(date_to_set)
        self.wait_for_element(self.dateToField).send_keys(Keys.ENTER)

        # делается клик в любое место на странице, что бы скрыть календарь
        self.wait_for_element("html/body").click()
        pass


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
