# -*- coding: utf-8 -*-
#
import Pagination
import inspect
import time
import myjson
from selenium.webdriver.common.keys import Keys
import init_driver


class ShopfrontQuickSignUp(init_driver.InitDriver):

    b2b = ".//*[@id='menu']//*[@href='/ru/b2b/']"
    free = ".//*[@id='ipBlock-main']//a[contains(.,'Номер 8-800')]"
    did = ".//*[@id='ipBlock-main']//a[contains(.,'Многоканальный номер')]"
    choose_number_btn = ".//*[@id='ipBlock-main']//a[contains(.,'Выбрать номер')]"
    last_number_in_list = ".//*[@id='ipBlock-main']//table[@class='number-selection-left-table mb-table']" \
                          "//tr[last()]/*[1][text()]"
    register_with_number_btn = ".//*[@id='ipBlock-main']//div[@class='cart-sidebar-small']" \
                               "//button[contains(.,'Оформить')]"
    phone = ".//*[@id='CustomerRegistration_phone']"
    email = ".//*[@id='CustomerRegistration_email']"
    password = ".//*[@id='CustomerRegistration_password']"
    password_repeat = ".//*[@id='CustomerRegistration_repeatPassword']"
    continue_btn = ".//*[@id='registration-submit']"
    check_code_filed = ".//*[@id='CustomerVerification_code']"
    continue_btn2 = ".//*[@id='modal-check-phone-number']//button[contains(.,'Подтвердить')]"

    def go_to_shopfront_page(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def go_to_choose_number_page(self, number_type_page):
        def get_number_type_link(type_of_number):
            print(inspect.stack()[0][3])
            if type_of_number is 'free':
                return self.free
            elif type_of_number is 'did':
                return self.did

        print(inspect.stack()[0][3])
        self.wait_for_element(self.b2b).click()
        self.wait_for_element(get_number_type_link(type_of_number=number_type_page)).click()
        self.wait_for_element(self.choose_number_btn).click()

    def buy_any_number_in_list(self):
        """ Returns chosen number """
        print(inspect.stack()[0][3])
        self.wait_for_element('html/body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        Pagination.Pagination(self.driver).go_to_last_page_if_possible()
        self.wait_for_element('html/body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        number_to_return = self.wait_for_element(self.last_number_in_list).text
        self.wait_for_element(self.last_number_in_list).click()
        return number_to_return

    def register_with_number(self, number_to_register, email_to_register, password_to_register):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.register_with_number_btn).click()
        self.wait_for_element(self.phone).send_keys(number_to_register[1:])
        self.wait_for_element(self.email).send_keys(email_to_register)
        self.wait_for_element(self.password).send_keys(password_to_register)
        self.wait_for_element(self.password_repeat).send_keys(password_to_register)
        self.wait_for_element(self.continue_btn).click()
        sms_check_code = myjson.sms_check_code(number_to_get_sms_check_code=number_to_register)
        self.wait_for_element(self.check_code_filed).send_keys(sms_check_code)
        self.wait_for_element(self.continue_btn2).click()
