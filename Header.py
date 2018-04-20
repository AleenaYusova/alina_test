# -*- coding: utf-8 -*-
#
import Helper
import inspect
import time
import init_driver
from urllib.parse import urlparse


class Header(init_driver.InitDriver):

    lsNumberLocator = "//div[contains(@class,'header_adm')]//a[text()[contains(.,'Лицевой счет')]]/b"
    lsButton = "//div[contains(@class,'header_adm')]//a[text()[contains(.,'Лицевой счет')]]"
    balanceNumberLocator = "//div[contains(@class,'header_adm')]//a[text()[contains(.,'Баланс')]]/b/b"
    balanceButton = "//div[contains(@class,'header_adm')]//a[text()[contains(.,'Баланс')]]"
    adminButton = "//div[contains(@class,'header_adm')]//a[@title='Настройки пользователя']/b"
    cliHeaderLocator = "//div[contains(@class,'header_adm')]//*[@title='Определяемый номер']"
    adminInternalNumberLocator = "//*[@id='internal-number']/div"
    logoutButton = "//div[contains(@class,'header_adm')]//a[contains(.,'Выйти')]"
    homeButton = "//div[contains(@class,'header_adm')]//a[@class='header__link header__link_adm nav']"
    journalButton = "//div[contains(@class,'header_adm')]//a[@href='/journal' and text()='Журнал']"
    settingsButton = "//div[contains(@class,'header_adm')]//a[@href='/settings' and text()='Настройки']"
    servicesButton = "//div[contains(@class,'header_adm')]//a[@href='/services' and text()='Услуги']"
    accountingButton = "//div[contains(@class,'header_adm')]//a[@href='/accounting' and text()='Оплата']"
    supportButton = "//div[contains(@class,'header_adm')]//a[@href='/support' and text()='Поддержка']"

    def click_account_number(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.lsButton).click()

    def get_account_number(self):
        print(inspect.stack()[0][3])
        account_number = self.wait_for_element(self.lsNumberLocator).text
        return account_number
        pass

    def click_balance(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.balanceButton).click()
        pass

    def get_balance(self):
        print(inspect.stack()[0][3])
        balance = self.wait_for_element(self.balanceNumberLocator).text
        balance = balance.replace(' ', '')
        return balance
        pass

    def click_admin(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.adminButton).click()
        pass

    def get_cli_origin_number_type(self):
        # print(inspect.stack()[0][3])
        # cliNumber = CLI.getCLIOriginNumberType(self.cliHeaderLocator)
        # return cliNumber
        pass

    def get_cli_clean_number_type(self):
        # print(inspect.stack()[0][3])
        # cliNumber = CLI.getCLICleanNumberType(self.cliHeaderLocator)
        # return cliNumber
        pass

    def get_admin_internal_number(self):
        print(inspect.stack()[0][3])
        internalnumber = self.wait_for_element(self.adminInternalNumberLocator).text
        internalnumber = internalnumber[-3:]
        return internalnumber
        pass

    def log_out(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc
        self.driver.get(new_url)
        time.sleep(1)
        self.wait_for_element(self.logoutButton).click()

    def click_home_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homeButton).click()
        pass

    def click_journal_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.journalButton).click()
        pass

    def click_settings_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.settingsButton).click()
        pass

    def click_services_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.servicesButton).click()
        pass

    def click_accounting_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.accountingButton).click()
        pass

    def click_support_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.supportButton).click()
        pass

    def take_a_screenshot_in_base64_format(self):
        print(inspect.stack()[0][3])
        Helper.ScreenShot(self.driver).take_screen_shot_in_base64_format()
