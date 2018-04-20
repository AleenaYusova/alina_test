# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import Helper
import time
import SetUpFile
import init_driver


class VoiceMailPage(init_driver.InitDriver):

    url_path = "/journal/voiceMail"
    title = "Голосовая почта"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Голосовая почта')]"
    number_in_first_line_of_table = ".//*[@id='journal_data']/div[2]/div[1]/b"
    first_part_of_xpath = ".//*[@id='journal_data']//b[contains(.,'"
    data_and_time_second_part = "')]/parent::div/span"
    to_whom_second_part = "')]/parent::div/parent::div/div[2]"
    download_voice_mail_btn = "')]/parent::div/parent::div/div[4]/*"
    play_voice_mail_btn = "')]/parent::div/parent::div/div//a[@class='layout__play-bg play-button']"
    delete_voice_mail_btn = "')]/parent::div/parent::div/div//" \
                            "a[@class='layout__basket-bg-bl layout__basket-bl_fl_r voicemail-delete']"
    download_excel_btn = "//a[contains(.,'Экспорт в Excel')]"

    def go_to_voice_mail_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_voice_mail_page(self):
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

    def get_voice_mail_number_in_first_line_of_table(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.number_in_first_line_of_table).text
        pass

    def get_voice_mail_date_and_time(self, number):
        print(inspect.stack()[0][3])
        number = Helper.GetFullNumber.get_full_number(number)
        return self.wait_for_element(self.first_part_of_xpath + str(number) + self.data_and_time_second_part).text
        pass

    def get_to_whom_voice_mail(self, number_who_called):
        print(inspect.stack()[0][3])
        number = Helper.GetFullNumber.get_full_number(number_who_called)
        return self.wait_for_element(self.first_part_of_xpath + str(number) + self.to_whom_second_part).text

    def download_voice_mail(self, number_who_called):
        print(inspect.stack()[0][3])
        number = Helper.GetFullNumber.get_full_number(number_who_called)
        self.wait_for_element(self.first_part_of_xpath + str(number) + self.download_voice_mail_btn).click()

    def listen_to_voice_mail(self, number_who_called):
        print(inspect.stack()[0][3])
        number = Helper.GetFullNumber.get_full_number(number_who_called)
        self.wait_for_element(self.first_part_of_xpath + str(number) + self.play_voice_mail_btn).click()

    def delete_voice_mail(self, number_who_called):
        print(inspect.stack()[0][3])
        number = Helper.GetFullNumber.get_full_number(number_who_called)
        self.wait_for_element(self.first_part_of_xpath + str(number) + self.delete_voice_mail_btn).click()

    def download_export_excel(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.download_excel_btn).click()
        pass
