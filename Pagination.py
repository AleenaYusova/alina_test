# -*- coding: utf-8 -*-
#
import time
from selenium.webdriver.common.keys import Keys
import init_driver


class Pagination(init_driver.InitDriver):

    pagination_existence = "//*[@class='yiiPager']"
    get_number_of_current_page = "//*[@class='yiiPager']/li[@class='page selected']//*"
    go_to_page = "//*[@class='yiiPager']/li[@class='page']//a[text()='"
    last_page = "//*[@class='yiiPager']/li[@class='page'][last()]"

    def go_to_next_page_if_possible(self):
        """ Если проверка на наличие пагинатора возвращает True """
        if self.check_if_there_is_pagination() is True:
            self.driver.find_element_by_xpath("html/body").send_keys(Keys.END)
            current_page_number = self.wait_for_element(self.get_number_of_current_page).text
            int_current_page_number = int(current_page_number)
            int_current_page_number = int_current_page_number + 1

            """Делается попытка сделать клик следующей страницы."""
            try:
                self.driver.find_element_by_xpath("html/body").send_keys(Keys.DOWN)
                xpath = (self.go_to_page + str(int_current_page_number) + "']")
                time.sleep(2)
                self.wait_for_element(str(xpath)).click()
                self.driver.find_element_by_xpath("html/body").send_keys(Keys.HOME)
            except UserWarning:
                self.driver.find_element_by_xpath("html/body").send_keys(Keys.HOME)

        elif self.check_if_there_is_pagination() is False:
            return None

    def go_to_last_page_if_possible(self):
        """ Если проверка на наличие пагинатора возвращает True """
        if self.check_if_there_is_pagination() is True:
            """ Переход на последную страницу"""
            self.driver.find_element_by_xpath("html/body").send_keys(Keys.END)
            self.driver.find_element_by_xpath("html/body").send_keys(Keys.DOWN)
            time.sleep(2)
            self.driver.find_element_by_xpath(self.last_page).click()
        elif self.check_if_there_is_pagination() is False:
            return None

    def check_if_there_is_pagination(self):
        """ Делает проверку на наличие пагинатора.
            Возвращается True or False. """
        try:
            time.sleep(3)
            self.driver.find_element_by_xpath(self.pagination_existence)
            return True
        except UserWarning:
            return False
