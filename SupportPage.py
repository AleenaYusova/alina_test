# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import init_driver
import SetUpFile


class SupportPage(init_driver.InitDriver):

    url_path_faq_page = "/support"
    q_and_a_title = "Вопросы и ответы"
    faq_page_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Вопросы и ответы')]"
    search_field = ".//*[@id='faq-search-container']//form/input"
    search_btn = ".//*[@id='faq-search-container']//form/button"
    callback_instruction = ".//*[@id='faq-search-container']//a[contains(.,'Инструкция')]"
    feedback_page_title = "Обратная связь"
    url_path_feedback_page = "/support/feedback"
    feedback_page_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Обратная связь')]"
    feedback_dropdown = ".//*[@id='Feedback_topic-styler']"
    feedback_dropdown_element_in_list = ".//*[@id='Feedback_topic-styler']//li[contains(.,'Настройка')]"
    feedback_message_field = ".//*[@id='Feedback_message']"
    feedback_send_btn = ".//*[@id='contact-form']//button[@class='button-red feedback-send']"
    url_path_technical_map = "/support/customerCard"
    technical_map_title = "Техническая карта"
    technical_map_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Техническая карта')]"
    company_industry_dropdown = ".//*[@id='CustomerCard_company_scope-styler']"
    company_industry_dropdown_element = ".//*[@id='CustomerCard_company_scope-styler']//li[contains(.,'технологии')]"
    company_equipment_dropdown = "//*[@id='CustomerCard_equipment_type-styler']"
    company_equipment_dropdown_element = "//*[@id='CustomerCard_equipment_type-styler']//li[contains(.,'IP')]"
    technical_map_save_btn = ".//*[@id='yw0']//input[@value='Сохранить']"

    def go_to_faq_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path_faq_page
        self.driver.get(new_url)
        pass

    """ TO DO https://jira.mtt.ru:8443/browse/MTTBPORTAL-5706 """
    def make_sure_its_faq_page(self):
        """ сравнение title страницы """
        self.wait_for_element(self.faq_page_navigationBarElement).click()
        time.sleep(3)
        assert self.driver.title in self.q_and_a_title
        pass

    def search_faq(self):
        self.wait_for_element(self.search_field).clear()
        self.wait_for_element(self.search_field).send_keys("callback")
        self.wait_for_element(self.search_btn).click()
        self.wait_for_element(self.callback_instruction).click()
        pass

    def go_to_feedback_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path_feedback_page
        self.driver.get(new_url)
        pass

    def make_sure_its_feedback_page(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path +
                                               self.url_path_feedback_page)
            pass

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            self.wait_for_element(self.feedback_page_navigationBarElement).click()
            time.sleep(3)
            assert self.driver.title in self.feedback_page_title
            pass

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()
        pass

    def send_feedback(self):
        self.wait_for_element(self.feedback_dropdown).click()
        self.wait_for_element(self.feedback_dropdown_element_in_list).click()
        self.wait_for_element(self.feedback_message_field).send_text("test message")
        self.wait_for_element(self.feedback_send_btn).click()
        pass

    def go_to_action_technical_map(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path_technical_map
        self.driver.get(new_url)
        pass

    def make_sure_its_technical_map(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path +
                                               self.url_path_technical_map)
            pass

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            self.wait_for_element(self.technical_map_navigationBarElement).click()
            time.sleep(3)
            assert self.driver.title in self.technical_map_title
            pass

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()
        pass

    def fill_and_save_technical_map(self):
        self.wait_for_element(self.company_industry_dropdown).click()
        self.wait_for_element(self.company_industry_dropdown_element).click()
        self.wait_for_element(self.company_equipment_dropdown).click()
        self.wait_for_element(self.company_equipment_dropdown_element).click()
        self.wait_for_element(self.technical_map_save_btn).click()
        pass
