# -*- coding: utf-8 -*-
#
import inspect
import unittest
import sys
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class CallbackSettingsPage(init_driver.InitDriver):

    url_path = "/settings/callback"
    title = "Настройки Callback"
    navigationBarElement = "//*[@class='lR__it nav lR__it_active'][text()='Callback']"
    pageTitleElement = "//h1[@class='basket__title basket__title_adm'][text()='Настройки Callback']"
    addCallbackBtn = ".//*[@id='callback-add-lock']//a[text()='Подключить']"
    openCallbackFirstPartOfXpath = ".//*[@id='callback-add-lock']//a[contains(.,'"
    openCallbackSecondPartOfXpath = "')]//parent::div/parent::div" \
                                    "//a[@class='callback-settings-link layout__basket-cogwheel-bg delete-button']"

    def go_to_callback_settings_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_callback_settings_page(self):
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

    def add_callback_on_settings_page(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.addCallbackBtn).click()
        pass

    def go_callback(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.navigationBarElement).click()
        pass

    def open_callback_settings_popup(self, callback_name):
        print(inspect.stack()[0][3])
        # оставляем только первые 15 символов от названия сайта, т.к. если название слишком большое,
        # оно может не отобразиться на странице полностью, и => selenium не найдет элемент на странице
        callback_name = callback_name[:15]
        self.wait_for_element(self.openCallbackFirstPartOfXpath + str(callback_name)
                              + self.openCallbackSecondPartOfXpath).click()
        pass

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
