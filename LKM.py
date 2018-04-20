# -*- coding: utf-8 -*-
#
import myjson
import sqltestfile
import inspect
from urllib.parse import urlparse
import time
import init_driver
import Helper
import SetUpFile
import TestSuiteSmokeTestLKA
import Login
import Pagination


class LKM(init_driver.InitDriver):

    url_path = "/manager/administration"
    login_filter = ".//*[@id='CustomersFilter_login']"
    search_btn = ".//*[@id='filter-form']//input[@class='button-red button-red_abc filter-submit']"
    icon = ".//*[@id='item-list-container']//*[@class='layout__basket-cogwheel cogwheel-menu']"
    change_manager_btn = ".//*[@id='item-list-container']//ul/li/a[contains(.,'Сменить менеджера')]"
    delete_customer_btn = ".//*[@id='item-list-container']//ul/li/a[contains(.,'Удалить тестовый ЛС')]"
    cancel_sign_contract_on_customer_btn = ".//*[@id='item-list-container']" \
                                           "//ul/li/a[contains(.,'Cбросить подпись клиента на договоре')]"
    sign_contract_btn = ".//*[@id='item-list-container']//ul/li/a[contains(.,'Подписание договора')]"
    manager_dropdown_list = ".//*[@id='Customer_managerId-styler']"
    manager_name = "Automated Test"
    manager_list = ".//*[@id='Customer_managerId-styler']/div[2]/ul/li[contains(.,'"
    change_manager_save_btn = ".//*[@id='change-manager-dialog']//input[@type='submit' and @value='Сменить']"
    login_field = ".//*[@id='ManagerLoginForm_email']"
    password_field = ".//*[@id='ManagerLoginForm_password']"
    login_btn = ".//*[@id='login-form']//input[@type='submit' and @value='Войти']"
    confirm_delete_btn = "//div[@class='ui-dialog-buttonset']//*[@class='ui-button-text'][contains(.,'Согласен')]"
    confirm_delete_ok_btn = "html/body/div/div/div/button[contains(.,'OK')]"
    view_documents_btn = ".//*[@id='item-list-container']/div[2]/div[6]/a[@title='Документы']"
    generate_documents_btn = "//button[@class='button-red temp-document-generate']"
    document_in_list = ".//*[@id='item-list-container']/div[@class='clearfix basket__line see_doc document-row']"
    logoutButton = "//div[contains(@class,'header_adm')]//a[contains(.,'Выйти')]"
    customer_type_dropdown = ".//*[@id='AddCustomerCommonData_customerType-styler']"
    add_customer_btn = "//button[@class='button-red customer-add']"
    juridical_type = ".//*[@id='AddCustomerCommonData_customerType-styler']//ul/li[contains(.,'Юридическое лицо')]"
    physical_type = ".//*[@id='AddCustomerCommonData_customerType-styler']//ul/li[contains(.,'Физическое лицо')]"
    payment_type_dropdown = ".//*[@id='AddCustomerCommonData_paymentType-styler']"
    prepayment = ".//*[@id='AddCustomerCommonData_paymentType-styler']//ul/li[contains(.,'Аванс')]"
    credit = ".//*[@id='AddCustomerCommonData_paymentType-styler']//ul/li[contains(.,'Кредит')]"
    customer_email = ".//*[@id='AddCustomerCommonData_email']"
    customer_phone = ".//*[@id='AddCustomerCommonData_phone']"
    save_btn = ".//*[@id='customerData-form']//*[@type='submit' and @value='Сохранить']"
    add_vpbx_btn = "//a[@item-type='vpbx']"
    create_customer_btn = "//button[@class='button-red action-create-customer']"
    give_access = ".//*[@id='item-list-container']//a[contains(.,'Предоставить доступ')]"
    confirm_give_access = "//div[@class='ui-dialog-buttonset']//*[contains(.,'Предоставить доступ')]"
    after_give_access = "//*[@class='ui-dialog-buttonset']//*[contains(.,'OK')]"
    insert_password = "//input[@id='CustomerPasswordChange_password' and @type='password']"
    insert_password_again = "//input[@id='CustomerPasswordChange_repeatPassword' and @type='password']"
    save_password_btn = "//input[@type='submit' and @value='Сохранить']"
    ok_btn = "//button[contains(.,'OK')]"
    check_code_for_giving_access = "//input[@id='CustomerVerification_code']"
    agree_check_box = "//*[@id='agree-styler']"
    confirm_btn = "//*[@value='Подтвердить']"
    icon_btn_to_set_credit_limit = "//div[@id='item-list-container']//div[2]" \
                                   "//a[@class='layout__basket-check select-change-payment-type'][1]"
    credit_limit_field = "//div[@class='popup clearfix']//input[@name='ChangePaymentType[creditLimit]']"
    save_credit_limit_btn = "//div[@class='popup clearfix']//input[@value='Установить']"
    activate_credit_customer_btn = "//div[@class='popup clearfix']//input[@value='Активировать']"
    choose_number_btn = "//a[contains(.,'Выбрать номер')]"
    type_number_dropdown = "//*[@id='type-styler']/div"
    did_type = "//*[@id='type-styler']//ul/li[contains(.,'Городской')]"
    free_type = "//*[@id='type-styler']//ul/li[contains(.,'800')]"
    mobile_type = "//*[@id='type-styler']//ul/li[contains(.,'Мобильный')]"
    phone_number_in_table = "//table[@class='number-selection-left-table mb-table']//tr[last()]/td[1]"
    phone_buy_icon_in_table = "//table[@class='number-selection-left-table mb-table']" \
                              "//tr[last()]/td[last()]/a[@number='"
    conditions_popup = "//*[@class='popup__underwrap']//*[@value='Добавить']"
    back_btn = "//*[@value='Вернуться']"
    add_package_btn = "//div[@class='clearfix']//button[contains(.,'Добавить пакет')]"
    no_package_btn = "//a[@class='link-dashed link-dashed_margin_left action-no-package']"
    package_list = "//div[@class='popup__underwrap']//*[@id='PackageProductConfigurator_packageId-styler']"
    package_sales_office = "//div[@class='popup__underwrap']//ul/li[contains(.,'Офис продаж')]"
    select_package_btn = "//div[@class='popup__underwrap']//button[@class='button-red button-red_float_right package-save']"
    add_did_within_package = "//a[@class='link-dashed action-choose-number'][@data-restriction-type='did_number']"
    add_free_within_package = "//a[@class='link-dashed action-choose-number'][@data-restriction-type='free_number']"

    def go_to_lkm(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def login_lkm(self, url, email, password):
        print(inspect.stack()[0][3])
        self.driver.get(url)
        self.wait_for_element(self.login_field).send_keys(email)
        self.wait_for_element(self.password_field).send_keys(password)
        self.wait_for_element(self.login_btn).click()
        time.sleep(3)

    def search_customer(self, customer_email):
        print(inspect.stack()[0][3])
        self.go_to_lkm()
        self.wait_for_element(self.login_filter).send_keys(customer_email)
        self.wait_for_element(self.search_btn).click()
        time.sleep(3)

    def delete_customer(self, customer_email):
        print(inspect.stack()[0][3])
        self.search_customer(customer_email=customer_email)
        time.sleep(0.5)
        print("Helper.ActionChainsClass(self.driver).move_to_element_and_click(self.icon, self.change_manager_btn)")
        Helper.ActionChainsClass(self.driver).move_to_element_and_click(self.icon, self.change_manager_btn)
        time.sleep(0.5)
        self.wait_for_element(self.manager_dropdown_list).click()
        self.wait_for_element(self.manager_list + self.manager_name + "')]").click()
        self.wait_for_element(self.change_manager_save_btn).click()
        time.sleep(1)
        self.search_customer(customer_email=customer_email)
        try:
            Helper.ActionChainsClass(self.driver).move_to_element_and_click(
                self.icon, self.cancel_sign_contract_on_customer_btn)
            time.sleep(3)
            self.search_customer(customer_email=customer_email)
        finally:
            Helper.ActionChainsClass(self.driver).move_to_element_and_click(self.icon, self.delete_customer_btn)
            time.sleep(3)
            self.wait_for_element(self.confirm_delete_btn).click()
            time.sleep(12)
            self.wait_for_element(self.confirm_delete_ok_btn).click()
            self.search_customer(customer_email=customer_email)
            try:
                self.driver.find_element_by_xpath(self.icon)
                print(print(inspect.stack()[0][3]) + " CUSTOMER MIGHT WAS NOT BEEN DELETED")
                print(Warning)
                return False
            except Warning:
                return True

    def find_customer_and_sign_contract(self, customer_email_login):
        print(inspect.stack()[0][3])
        self.search_customer(customer_email=customer_email_login)
        Helper.ActionChainsClass(self.driver).move_to_element_and_click(self.icon, self.sign_contract_btn)
        time.sleep(8)

    def find_customer_and_generate_documents_for_her(self, customer_email_to_generate_docs):
        print(inspect.stack()[0][3])
        self.search_customer(customer_email=customer_email_to_generate_docs)
        self.wait_for_element(self.view_documents_btn).click()
        self.wait_for_element(self.generate_documents_btn).click()
        time.sleep(10)
        self.wait_for_element(self.document_in_list)

    def log_out_from_lkm(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + '/manager/administration'
        self.driver.get(new_url)
        time.sleep(1)
        self.wait_for_element(self.logoutButton).click()

    def register_customer_on_lkm(self, customer_type_juridical_or_physical, payment_type_prepayment_or_credit,
                                 customer_email, customer_phone_number, with_package=True,
                                 buy_did=True, buy_free=False, buy_mobile=False):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.add_customer_btn).click()
        self.wait_for_element(self.customer_type_dropdown).click()

        ''' Если при вызове метода передан тип юридический то юридический
            Если физический то физический'''
        if customer_type_juridical_or_physical is 'juridical':
            self.driver.find_element_by_xpath(self.juridical_type).click()
        elif customer_type_juridical_or_physical is 'physical':
            self.driver.find_element_by_xpath(self.physical_type).click()
        else:
            return AttributeError

        self.wait_for_element(self.payment_type_dropdown).click()

        ''' Если при вызове метода передан платежный тип авансовые то авансовые. 
            Если кредитный то кредитный'''
        if payment_type_prepayment_or_credit is 'prepayment':
            self.driver.find_element_by_xpath(self.prepayment).click()
        elif payment_type_prepayment_or_credit is 'credit':
            self.driver.find_element_by_xpath(self.credit).click()
        else:
            return AttributeError

        self.wait_for_element(self.customer_email).send_keys(customer_email)
        self.wait_for_element(self.customer_phone).send_keys(customer_phone_number[1:])
        self.wait_for_element(self.save_btn).click()

        ''' Если при вызове метода передан True для параметра "С пакетом", 
            то проигрывается сценарий с пакетом.
            Если нет, то нажимается кнопка без пакета, и продолжается регистрация'''
        if with_package is True:
            time.sleep(1)
            self.driver.find_element_by_xpath(self.add_package_btn).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath(self.package_list).click()
            self.driver.find_element_by_xpath(self.package_sales_office).click()
            self.driver.find_element_by_xpath(self.select_package_btn).click()
        elif with_package is False:
            time.sleep(1)
            self.driver.find_element_by_xpath(self.no_package_btn).click()
        else:
            return AttributeError

        '''В переменную записывается список покупаемых номеров. Список возвращается из метода choose_number'''
        list_of_bought_numbers = self.choose_number(buy_did=buy_did,
                                                    buy_free=buy_free,
                                                    buy_mobile=buy_mobile,
                                                    within_package=with_package)
        print(list_of_bought_numbers)
        self.wait_for_element(self.create_customer_btn).click()
        time.sleep(8)

    def choose_number(self, buy_did=False, buy_free=False, buy_mobile=False, within_package=False):
        """ метод возвращает список купленных номеров телефонов"""

        def buying_number():
            """внутри метода choose_number вызывается buying_number -- что является алгоритмом покупки номера"""
            print(inspect.stack()[0][3])
            Pagination.Pagination(self.driver).go_to_last_page_if_possible()
            phone_number = self.wait_for_element(self.phone_number_in_table).text
            phone_number = Helper.GetShortNumber.get_short_number(phone_number)
            self.wait_for_element(self.phone_buy_icon_in_table + str(phone_number) + "']").click()
            try:
                self.wait_for_element(self.conditions_popup).click()
            except:
                pass
            time.sleep(3)
            print(phone_number)
            return phone_number

        print(inspect.stack()[0][3])
        list_of_numbers_to_return = []

        if within_package is True:
            pass
        elif within_package is False:
            self.wait_for_element(self.choose_number_btn).click()
            self.wait_for_element(self.type_number_dropdown).click()

        if buy_did is True:
            try:
                self.wait_for_element(self.did_type).click()
            except:
                self.wait_for_element(self.add_did_within_package).click()
            did_number = buying_number()
            list_of_numbers_to_return.append(did_number)
        elif buy_did is False:
            pass

        if buy_free is True:
            try:
                self.wait_for_element(self.free_type).click()
            except:
                self.wait_for_element(self.add_free_within_package).click()
            free_number = buying_number()
            list_of_numbers_to_return.append(free_number)
        elif buy_free is False:
            pass

        if buy_mobile is True:
            self.wait_for_element(self.mobile_type).click()
            mobile_number = buying_number()
            list_of_numbers_to_return.append(mobile_number)
        elif buy_mobile is False:
            pass

        try:
            self.wait_for_element(self.back_btn).click()
        finally:
            return list_of_numbers_to_return

    def find_customer_set_credit_limit_and_activate(self, customer_email, credit_limit_amount):
        self.search_customer(customer_email=customer_email)
        self.wait_for_element(self.icon_btn_to_set_credit_limit).click()
        self.wait_for_element(self.credit_limit_field).clear()
        self.wait_for_element(self.credit_limit_field).send_keys(str(credit_limit_amount))
        self.wait_for_element(self.save_credit_limit_btn).click()
        self.go_to_lkm()
        self.search_customer(customer_email=customer_email)
        self.wait_for_element(self.icon_btn_to_set_credit_limit).click()
        self.wait_for_element(self.activate_credit_customer_btn).click()
        time.sleep(3)
        self.log_out_from_lkm()

    def find_customer_and_give_access_and_login_lka(self, customer_email, customer_phone_number):
        print(inspect.stack()[0][3])
        self.search_customer(customer_email=customer_email)
        self.wait_for_element(self.give_access).click()
        self.wait_for_element(self.confirm_give_access).click()
        self.wait_for_element(self.after_give_access).click()
        self.log_out_from_lkm()
        time.sleep(3)
        hash_code = sqltestfile.Query().query(customer_email=customer_email)
        link = SetUpFile.SetUpFile.lka_login_link + "/user/completePasswordRecovery?hash=" + str(hash_code)
        self.driver.get(link)
        time.sleep(1)
        self.wait_for_element(self.insert_password).send_keys(SetUpFile.SetUpFile.userPassword)
        self.wait_for_element(self.insert_password_again).send_keys(SetUpFile.SetUpFile.userPassword)
        self.wait_for_element(self.save_password_btn).click()
        time.sleep(7)
        # TO DO https://jira.mtt.ru:8443/browse/MTTBUSNS-3255
        try:
            Login.Login(self.driver).go_to_login(url_to_go=TestSuiteSmokeTestLKA.Config.lka_login_link)
            Login.Login(self.driver).insert_email(email=customer_email)
            Login.Login(self.driver).insert_password(password=TestSuiteSmokeTestLKA.Config.customer_password)
            Login.Login(self.driver).click_log_in_btn()
            check_code = myjson.sms_check_code(number_to_get_sms_check_code=customer_phone_number)
            self.wait_for_element(self.check_code_for_giving_access).send_keys(check_code)
            self.wait_for_element(self.agree_check_box).click()
            self.wait_for_element(self.confirm_btn).click()
        except UserWarning:
            return
