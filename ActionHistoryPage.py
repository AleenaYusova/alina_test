# -*- coding: utf-8 -*-
#
import inspect
import unittest
import sys
from urllib.parse import urlparse
import time
import init_driver
import SetUpFile


class ActionHistoryPage(init_driver.InitDriver):
    """
    Фильтры по истории действий не реализованы, до решения задачи:
    https://jira.mtt.ru:8443/browse/MTTBPORTAL-5681
    """

    url_path = "/journal/history"
    title = "История действий"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'История действий')]"
    firstTableLineDateAndTime = "//*[@id='history_data']//div[2]/div[1]"
    firstTableLineAction = "//*[@id='history_data']//div[2]/div[2]"
    firstTableLineNote = "//*[@id='history_data']//div[2]/div[3]"
    firstTableLineInitiator = "//*[@id='history_data']//div[2]/div[4]"
    actionHistoryExportBtn = ".//*[@id='download-csv']"

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

    def get_action_history_dateandtime(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.firstTableLineDateAndTime).text
        pass

    def get_action_history_action(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.firstTableLineAction).text
        pass

    def get_action_history_note(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.firstTableLineNote).text
        pass

    def get_action_history_initiator(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.firstTableLineInitiator).text
        pass

    def get_action_history_export(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.actionHistoryExportBtn).click()
        pass


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
