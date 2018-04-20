# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class ListOfLocators:
    """    Этот класс используется для присвоения имен.    """
    def __init__(self, box_btn, text_btn, fee):
        self.box_btn = box_btn
        self.text_btn = text_btn
        self.fee = fee


class ServicesPage(init_driver.InitDriver):

    url_path = "/services"
    title = "Услуги"
    navigationBarElement = "//a[@class='menu__a nav menu__a_active'][text()='Услуги']"
    total_charge_locator = ".//*[@id='yw1']//td[contains(.,'Всего абонентская плата')]/parent::*//b"
    first_part = ".//*[@id='yw1']//a[contains(.,'"
    second_part = "')]"
    box_part = "/parent::div/parent::div//img"
    fee_part_of_xpath = "/parent::div/parent::div//div[@class='basket__extra']"
    did = "Многоканальный городской номер"
    voip = "Исходящая связь VoIP"
    vpbx = "Виртуальная АТС"
    vr = "Запись разговоров"
    free = "Бесплатный вызов (8-800, 8-804)"
    mobile = "Мобильный номер"
    callback = "Callback"
    sim = "SIM-карта"

    def go_to_services_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_services_page(self):
        print(inspect.stack()[0][3])

        """ Проверка правильности пути в url 
        TO DO https://jira.mtt.ru:8443/browse/MTTBUSNS-4393 """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            self.wait_for_element(self.navigationBarElement).click()
            time.sleep(3)
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

    def get_total_charge(self):
        print(inspect.stack()[0][3])
        total_charge = self.wait_for_element(self.total_charge_locator).text
        total_charge = total_charge.replace(' ', '')
        return total_charge
        pass

    """
    Методы: click_text_of_service_name, click_box_of_service_name и get_fee_by_service_name
    Принимают в качестве входного параметра service_name_to_click.
    Что бы определить, название услуги (service name) происходит обращение к функции get_list_of_locators
    get_list_of_locators в свою очередь, в зависимости от переданного service name
    обращается к классу ListOfLocators и ее функции __init__, передавая в строгой последовательности
    box_btn (xpath для кликабельной коробки рядом с имененм услуги),
    text_btn (xpath для названия услуги),
    fee (xpath для столбца "Абонентская плата")
    """
    def click_box_of_service_name(self, service_name_to_click):
        print(inspect.stack()[0][3])
        pass
        self.wait_for_element(self.get_list_of_locators(service_name_to_click).box_btn).click()

    def click_text_of_service_name(self, service_name_to_click):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.get_list_of_locators(service_name_to_click).text_btn).click()
        pass

    def get_fee_by_service_name(self, service_name_to_click):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.get_list_of_locators(service_name_to_click).fee).click()
        pass

    def get_list_of_locators(self, service_name):
        """ Method returns_list_of_locators_depending_on_the_given attribute (service_name) """
        if service_name is 'did':
            return ListOfLocators(self.first_part + self.did + self.second_part,
                                  self.first_part + self.did + self.second_part+self.box_part,
                                  self.first_part + self.did + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'voip':
            return ListOfLocators(self.first_part + self.voip + self.second_part,
                                  self.first_part + self.voip + self.second_part+self.box_part,
                                  self.first_part + self.voip + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'vpbx':
            return ListOfLocators(self.first_part + self.vpbx + self.second_part,
                                  self.first_part + self.vpbx + self.second_part+self.box_part,
                                  self.first_part + self.vpbx + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'vr':
            return ListOfLocators(self.first_part + self.vr + self.second_part,
                                  self.first_part + self.vr + self.second_part+self.box_part,
                                  self.first_part + self.vr + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'free':
            return ListOfLocators(self.first_part + self.free + self.second_part,
                                  self.first_part + self.free + self.second_part+self.box_part,
                                  self.first_part + self.free + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'mobile':
            return ListOfLocators(self.first_part + self.mobile + self.second_part,
                                  self.first_part + self.mobile + self.second_part+self.box_part,
                                  self.first_part + self.mobile + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'callback':
            return ListOfLocators(self.first_part + self.callback + self.second_part,
                                  self.first_part + self.callback + self.second_part+self.box_part,
                                  self.first_part + self.callback + self.second_part+self.fee_part_of_xpath)
        elif service_name is 'sim':
            return ListOfLocators(self.first_part + self.sim + self.second_part,
                                  self.first_part + self.sim + self.second_part+self.box_part,
                                  self.first_part + self.sim + self.second_part+self.fee_part_of_xpath)
        else:
            print(AttributeError)
            return AttributeError
