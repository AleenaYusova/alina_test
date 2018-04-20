# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import init_driver
import SetUpFile


class VoiceRecordPage(init_driver.InitDriver):

    url_path = "/services/vr"
    title = "Запись разговоров"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Запись разговоров')]"
    vr_button = "//*[@id='vr-button']"
    monthly_fee_locator = ".//*[@id='voice_record']/div[2]/div/div[2]/div[2]/b"
    sign_btn = "//button[contains(.,'Подписать')]"
    cancel_sign_btn = "//button[contains(.,'Отмена')]"

    def go_to_voice_record_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_voice_record_page(self):
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

    def turn_record_on_or_off(self, sign_agreement=True):
        print(inspect.stack()[0][3])
        time.sleep(1)
        self.wait_for_element(self.vr_button).click()
        if sign_agreement is True:
            self.wait_for_element(self.sign_btn).click()
        elif sign_agreement is False:
            self.wait_for_element(self.cancel_sign_btn).click()

    def get_voice_record_monthly_fee(self):
        print(inspect.stack()[0][3])
        monthly_fee = self.wait_for_element(self.monthly_fee_locator).text
        return monthly_fee
        pass
