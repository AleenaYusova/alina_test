# -*- coding: utf-8 -*-
#
import inspect
import unittest
import sys
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class JournalCalls(init_driver.InitDriver):

    title = "Звонки"
    url_path = "/journal/calls"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Звонки')]"
    from_number_in_last_line = "//*[@id='journal_data']/div[2]/div[1]/b"
    to_number_in_last_line = ".//*[@id='journal_data']/div[2]/div[2]/text()"
    date_and_time_in_last_line = ".//*[@id='journal_data']/div[2]/div[3]/text()"
    duration_in_last_line = "//*[@id='journal_data']/div[2]/div[4]/text()"
    download_last_call = "//*[@id='journal_data']/div[2]/div[5]/a"
    listen_to_last_call = "//*[@id='journal_data']/div[2]/div[6]//a"
    download_excel = ".//*[@id='item-list-container']//a[contains(.,'Экспорт в Excel')]"

    def go_to_journal_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_journal_page(self):
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

    def get_call_from_number_in_last_line(self):
        """ Возвращает номер телефона в вехней строке табилцы, колонка 'От кого' """
        print(inspect.stack()[0][3])
        from_number = self.wait_for_element(self.from_number_in_last_line).text
        return from_number
        pass

    def get_call_to_number_in_last_line(self):
        """ Возвращает номер телефона в вехней строке табилцы, колонка 'Кому' """
        print(inspect.stack()[0][3])
        from_number = self.wait_for_element(self.to_number_in_last_line).text
        from_number = from_number.replace(' ', '')
        return from_number
        pass

    def get_date_and_time_in_last_line(self):
        """ Возвращает дату и время в вехней строке табилцы """
        print(inspect.stack()[0][3])
        from_number = self.wait_for_element(self.date_and_time_in_last_line).text
        from_number = from_number.replace(' ', '')
        return from_number
        pass

    def get_last_call_line_duration(self):
        """ Возвращает продолжительность разговора из вехней строки табилцы """
        print(inspect.stack()[0][3])
        from_number = self.wait_for_element(self.duration_in_last_line).text
        from_number = from_number.replace(' ', '')
        from_number = from_number.replace('сек', '')
        return from_number
        pass

    def download_calls_record(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.download_last_call).click()
        pass

    def listen_to_call_record(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.listen_to_last_call).click()
        pass

    def get_journal_export(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.download_excel).click()
        self.driver.set_page_load_timeout(60)
        pass

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
