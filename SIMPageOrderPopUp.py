# -*- coding: utf-8 -*-
#
from selenium.webdriver.common.keys import Keys
import init_driver


class SIMPageOrderPopUp(init_driver.InitDriver):

    text_in_region_element = ".//*[@id='OrderSimRegistration_regionDelivery-styler']//*[text()]"
    text_in_amount_element = ".//*[@id='OrderSimRegistration_countSim-styler']"
    last_name = "//*[@id='OrderSimRegistration_lastName']"
    first_name = "//*[@id='OrderSimRegistration_firstName']"
    middle_name = "//*[@id='OrderSimRegistration_middleName']"
    phone_number = "//*[@id='OrderSimRegistration_phone']"
    email = "//*[@id='OrderSimRegistration_email']"
    street = ".//*[@id='OrderSimRegistration_street']"
    house = ".//*[@id='OrderSimRegistration_house']"
    korpus = ".//*[@id='OrderSimRegistration_housing']"
    apartment = ".//*[@id='OrderSimRegistration_apartment']"
    index = ".//*[@id='OrderSimRegistration_index']"
    address_region = ".//*[@id='OrderSimRegistration_region']"
    address_city = ".//*[@id='OrderSimRegistration_city']"
    order_btn = ".//*[@id='modal-select-options']//button[contains(.,'Заказать')]"
    get_order_number = ".//*[@id='message-dialog']//div[contains(.,'Заказ №')]/b[1][text()]"

    def order_sim_popup_for_delivery(self):
        self.wait_for_element(self.last_name).send_keys("test last_name")
        self.wait_for_element(self.first_name).send_keys("test first_name")
        self.wait_for_element(self.middle_name).send_keys("test middle_name")
        self.wait_for_element(self.phone_number).send_keys("9876543210")
        self.wait_for_element(self.email).send_keys("test@auto.test")
        self.wait_for_element(self.street).send_keys("Мира")
        self.wait_for_element(self.street).send_keys(Keys.DOWN)
        self.wait_for_element(self.street).send_keys(Keys.ENTER)
        self.wait_for_element(self.house).send_keys("1")
        self.wait_for_element(self.korpus).send_keys("234")
        self.wait_for_element(self.apartment).send_keys("5")
        """ Ниже проходят проверки, полей, которые должны быть заполнен автоматически"""
        assert self.wait_for_element(self.text_in_region_element).text \
            in self.wait_for_element(self.address_region).text
        assert len(self.wait_for_element(self.index).text) in 6
        """ Возвращает номер заказа"""
        self.wait_for_element(self.order_btn).click()
        order_number = self.wait_for_element(self.get_order_number).text
        return order_number
        pass

    def order_sim_popup_for_pickup(self):
        self.wait_for_element(self.last_name).send_keys("test last_name")
        self.wait_for_element(self.first_name).send_keys("test first_name")
        self.wait_for_element(self.middle_name).send_keys("test middle_name")
        self.wait_for_element(self.phone_number).send_keys("9876543210")
        self.wait_for_element(self.email).send_keys("test@auto.test")
        self.wait_for_element(self.order_btn).click()
        """ Возвращает номер заказа"""
        order_number = self.wait_for_element(self.get_order_number).text
        return order_number
        pass

    def assert_in_region_and_sim_amount(self, region_should_be, amount_of_sim_cards_should_be):
        """ Проверка на совпадение региона и количества сим кард, переданных в SimPage.order_sim"""
        region_in_popup = self.wait_for_element(self.text_in_region_element).text
        assert region_in_popup in region_should_be
        amount_of_sim_cards_in_popup = self.wait_for_element(self.text_in_amount_element).text
        assert amount_of_sim_cards_in_popup in amount_of_sim_cards_should_be
