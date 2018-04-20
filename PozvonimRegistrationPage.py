# -*- coding: utf-8 -*-
#
import inspect
import time
import myjson
import json
import requests
import init_driver
import pyperclip


class PozvonimRegistrationPage(init_driver.InitDriver):

    phoneField = "//input[@id='mobile-phone']"
    emailField = "//input[@name='email']"
    passwordField = "//input[@type='password']"
    offerCheckbox = "//div[@class='accept-offer form-field has-success']/label/div"
    registrationButton = "//div[@class='form-button-box'][contains(.,'Зарегистрироваться')]"
    check_code_filed = "//input[@name='code']"
    continueButton = "//button[@id='register_button']"
    websiteField = "//input[@placeholder='example.com']"
    loginButton = "//div[@class='form-button-box'][contains(.,'Войти')]"
    managername_field = "//div[@class='form-group']/input[@name='name']"
    managerphone_field = "//div[@class='form-group']/input[@name='phone']"
    manageremail_field = "//div[@class='form-group']/input[@name='email']"
    managerlogin_field = "//div[@class='form-group']/input[@name='login']"
    managerpassword_field = "//div[@class='form-group']/input[@name='password']"
    continue_btn = "//button[@class='pull-right btn btn-success modal-ok-button'][contains(.,'Продолжить')]"
    profile_btn = "//li[@data-controller='Profile'][contains(.,'Профиль')]"
    passport_series_field = "//input[@name='passport_series']"
    passport_number_field = "//input[@name='passport_no']"
    date_of_issue_field = "//input[@name='passport_issued']"
    issued_by_field = "//input[@name='passport_issued_by']"
    passport_birth_place_field = "//input[@name='passport_birth_place']"
    passport_address_field = "//input[@name='passport_registr_addr']"
    passport_surname_field = "//input[@name='last_name']"
    passport_name_field = "//input[@name='first_name']"
    date_of_birth_field = "//input[@name='passport_birthdate']"
    save_btn = "//button[@class='btn btn-success'][contains(.,'Сохранить')]"
    pzv_signcontract_btn = "//button[@class='pull-right btn btn-success modal-ok-button'][contains(.,'Подписать')]"
    mttb_save_btn = "//a[@class='button-red contract-edit-submit'][contains(.,'Сохранить')]"
    mttb_services_btn = "//a[@class='menu__a nav'][contains(.,'Услуги')]"
    mttb_web_widgets_btn = "//a[@class='lR__it  nav'][contains(.,'Web-виджеты')]"
    mttb_to_plug_ww_btn = "//a[@class='button-red'][contains(.,'Подключить')]"
    web_widget_btn = "//li[@class='has_sub'][contains(.,'Web-виджеты')]"
    event_btn = "//li[@class='has_sub'][contains(.,'События')]"
    statistic_btn = "//li[@class='has_sub'][contains(.,'Статистика')]"
    addproject_btn = "//button[@onclick='Controller.Sites().Modal.create();'][contains(.,'Добавить проект')]"
    success_btn = "//button[@class='btn btn-red padding-left-40 padding-right-40'][contains(.,'Далее')]"
    close_btn_once = "//div[@class='modal-header']/button[@type='button']"
    close_btn_twice = "//div[@class='modal-header']/button[@data-dismiss='modal']"
    managers_btn = "//li[@data-controller='Managers'][contains(.,'Менеджеры')]"
    one_free_operator_btn = "//button[@class='btn btn-warning btn-sm margin-left-10'][contains(.,'Активировать 1 оператора бесплатно')]"
    try_free_btn = "//button[@class='pull-right btn btn-success modal-ok-button'][contains(.,'Попробовать бесплатно')]"
    addplaces_btn = "//button[@class='btn btn-warning btn-sm'][contains(.,'Добавить места')]"
    pay_for_places_btn = "//button[@class='pull-right btn btn-red modal-ok-button'][contains(.,'Оплатить')]"
    addmanager_btn = "//div[contains(@class,'add-operator-button')]/button"
    operators_btn = "//select[@class='form-control']"
    create_new_operator_btn = "//button[@data-type='agent'][contains(.,'Создать нового оператора')]"
    site_title = "//div[contains(@class, 'site-list-managers-row')]"
    managerfield_null_btn = "//div[@class='clearfix']"
    checkbox_service_first_xpath = "//div[contains(.,'"
    checkbox_service_second_xpath = "')]/label/div"
    checkbox_access_callback = "//div[contains(.,'Менеджер может принимать звонки')]/label/div"
    checkbox_access_premium = "//div[contains(.,'Менеджер может общаться в чате')]/label/div"
    create_manager_btn = "//button[@class='btn btn-red'][contains(.,'Создать менеджера')]"
    premium_free_btn = "//span[@class='button-text'][contains(.,'Премиум бесплатно')]"
    demo_callback_free_btn = "//a[@class='button btn btn-lg btn-block btn-info public'][contains(.,'Попробовать бесплатно')]"
    set_widget = "//span[@class=' widget-disabled']"
    set_chat = "//div[@class='col-sm-4 sites-list-cell _buttons']/button[@class='sites-list-module-button _extend'][contains(.,'Подключить')]"
    code_for_site = "//button[@class='btn button-agent-url button-agent-url-in-sites-list'][contains(.,'Код на сайт')]"
    copy_code_for_site = "//button[@class='btn btn-red copy-code-button'][contains(.,'Скопировать код в буфер')]"
    landing_btn ="//a[@class='sites-list-site-header-link'][contains(.,'landing.pozvonim.rnd.mtt')]"
    landing_site = "//div[@class='navbar-header']"


    def go_to_pzv_registration(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def insert_phone(self, phone):
        print(inspect.stack()[0][3])
        time.sleep(1)
        self.wait_for_element(self.phoneField).clear()
        time.sleep(1)
        self.wait_for_element(self.phoneField).send_keys(phone[1:])

    def insert_email(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.emailField).send_keys(email)

    def insert_password(self, password):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordField).send_keys(password)

    def click_accept_offer(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.offerCheckbox).click()

    def click_log_in_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.registrationButton).click()
        time.sleep(3)

    def sms_check_code(self, number_to_register):
        print(inspect.stack()[0][3])
        time.sleep(10)
        sms_check_code = myjson.sms_check_code(number_to_get_sms_check_code=number_to_register)
        self.wait_for_element(self.check_code_filed).send_keys(sms_check_code)
        time.sleep(3)
        self.wait_for_element(self.continueButton).click()
        time.sleep(15)

    def profile_btn_click(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.profile_btn).click()
        time.sleep(5)

    def refresh_page(self):
        time.sleep(120)
        self.driver.refresh()
        time.sleep(3)

    # def click_continue_btn(self):
    #     print(inspect.stack()[0][3])
    #     self.wait_for_element(self.continue_btn).click()
    #     time.sleep(10)

    def click_profile_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.profile_btn).click()
        time.sleep(3)

    def insert_passport_series(self,passport_series):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_series_field).send_keys(passport_series)
        time.sleep(3)

    def insert_passport_number(self,passport_number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_number_field).send_keys(passport_number)
        time.sleep(3)

    def insert_date_of_issue(self, date_of_issue):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.date_of_issue_field).send_keys(date_of_issue)
        time.sleep(3)

    def insert_issued_by(self,issued_by):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.issued_by_field).send_keys(issued_by)
        time.sleep(3)

    def insert_passport_birth_place(self,passport_birth_place):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_birth_place_field).send_keys(passport_birth_place)
        time.sleep(3)

    def insert_passport_address(self, passport_address):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_address_field).send_keys(passport_address)
        time.sleep(3)

    def insert_passport_surname(self, passport_surname):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_surname_field).send_keys(passport_surname)
        time.sleep(3)

    def insert_passport_name(self, passport_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passport_name_field).send_keys(passport_name)
        time.sleep(3)

    def insert_date_of_birth(self, date_of_birth):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.date_of_birth_field).send_keys(date_of_birth)
        time.sleep(3)

    def click_save_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.save_btn).click()
        time.sleep(5)

    def click_pzv_signcontract_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.pzv_signcontract_btn).click()
        time.sleep(3)

    def click_mttb_save_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_save_btn).click()
        time.sleep(3)

    def click_mttb_services_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_services_btn).click()
        time.sleep(3)

    def click_mttb_web_widgets_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_web_widgets_btn).click()
        time.sleep(4)

    def click_mttb_to_plug_ww_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_to_plug_ww_btn).click()
        time.sleep(4)

    def click_web_widget_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.web_widget_btn).click()
        time.sleep(3)

    def click_addproject_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.addproject_btn).click()
        time.sleep(3)

    def select_webwidgets(self, callback=None, chat=None, feedback=None, herdinstinct=None):
        print(inspect.stack()[0][3])
        dict_of_webwidgets_names = {
            callback: "Умный виджет обратной связи",
            chat: "Виджет онлайн консультанта",
            feedback: "Оценка качества",
            herdinstinct: "Стадное чувство",
        }

        for i in [callback, chat, feedback, herdinstinct]:
            if i is None:
                pass
            elif i is not None:
                xpath = (self.checkbox_service_first_xpath +
                         str(dict_of_webwidgets_names.get(i)) +
                            self.checkbox_service_second_xpath)
                print(xpath)
                self.wait_for_element(xpath).click()

    def insert_website(self, website):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.websiteField).send_keys(website)

    def click_success_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.success_btn).click()
        time.sleep(6)
        self.wait_for_element(self.close_btn_once).click()
        time.sleep(3)
        self.wait_for_element(self.close_btn_twice).click()
        time.sleep(3)

    def click_managers_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.managers_btn).click()
        time.sleep(3)

    def click_one_free_operator_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.one_free_operator_btn).click()
        time.sleep(4)

    def click_try_free_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.try_free_btn).click()
        time.sleep(5)

    def click_addmanager_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.site_title).click()
        self.wait_for_element(self.addmanager_btn).click()
        time.sleep(5)

    def click_create_new_operator_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.create_new_operator_btn).click()
        time.sleep(3)

    def insert_manager_name(self, managername):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.managername_field).send_keys(managername)
        time.sleep(3)

    def insert_manager_phone(self, managerphone):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.managerphone_field).send_keys(managerphone)
        time.sleep(3)

    def insert_manager_email(self, manageremail):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.manageremail_field).send_keys(manageremail)
        time.sleep(3)

    def insert_manager_login(self, managerlogin):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.managerlogin_field).send_keys(managerlogin)
        time.sleep(3)

    def insert_manager_password(self, managerpassword):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.managerpassword_field).send_keys(managerpassword)
        time.sleep(3)

    def click_checkbox_access_callback(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.checkbox_access_callback).click()
        time.sleep(3)

    def click_checkbox_access_premium(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.checkbox_access_premium).click()
        time.sleep(3)

    def click_create_manager_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.create_manager_btn).click()
        time.sleep(15)
        self.wait_for_element(self.managerfield_null_btn).click()
        time.sleep(5)

    def click_web_widget_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.web_widget_btn).click()
        time.sleep(3)

    def click_premium_free_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.premium_free_btn).click()
        time.sleep(5)

    def click_demo_callback_free_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.demo_callback_free_btn).click()
        time.sleep(5)

    def click_set_widget(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.set_widget).click()
        time.sleep(5)

    # def click_set_chat(self):
    #     print(inspect.stack()[0][3])
    #     self.wait_for_element(self.set_chat).click()
    #     time.sleep(5)

    def click_code_for_site(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.code_for_site).click()
        time.sleep(3)

    def click_copy_code_for_site(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.copy_code_for_site).click()
        time.sleep(3)
        self.wait_for_element(self.close_btn_twice).click()
        time.sleep(7)

    def click_landing_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.landing_btn).click()
        time.sleep(7)

    def click_landing_btn_in_site(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.landing_btn).click()
        time.sleep(7)


    # def click_addplaces_btn(self):
    #     print(inspect.stack()[0][3])
    #     self.wait_for_element(self.addplaces_btn).click()
    #     time.sleep(3)
    #
    # def click_operators_btn(self):
    #     print(inspect.stack()[0][3])
    #     self.wait_for_element(self.operators_btn).click()
    #     time.sleep(3)
    #
    # def click_pay_for_places_btn(self):
    #      print(inspect.stack()[0][3])
    #      self.wait_for_element(self.pay_for_places_btn).click()
    #      time.sleep(3)
