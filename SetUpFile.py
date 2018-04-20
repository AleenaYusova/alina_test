# -*- coding: utf-8 -*-
#
from selenium import webdriver
import configparser
import inspect
import PozvonimStartPage
import PozvonimLoginPage
import PozvonimLandingPage
import PozvonimRegistrationPage
import PozvonimMainPage
import MTTB_Page
import sqltestfile
import traceback
import unittest


class SetUpFile(unittest.TestCase):

    def setUp(self):
        """ Запуск драйвера по умолчанию"""
        self.driver = webdriver.Chrome()
        """ Расширение окна браузера на полный экран"""
        self.driver.maximize_window()
        # self.driver.implicitly_wait(60)
        # """ Переход по URL из конфиг.файла"""
        # self.driver.get(self.url_path)

        """ Присваивание классов страниц
        Если вы создали новый файл, добавьте его в этот список"""
        self.sql = sqltestfile.Query()
        self.pozvonim_start_page = PozvonimStartPage.PozvonimStartPage(self.driver)
        self.pozvonim_login_page = PozvonimLoginPage.PozvonimLoginPage(self.driver)
        self.pozvonim_registration_page = PozvonimRegistrationPage.PozvonimRegistrationPage(self.driver)
        self.pozvonim_landing_page = PozvonimLandingPage.PozvonimLandingPage(self.driver)
        self.pozvonim_main_page = PozvonimMainPage.PozvonimMainPage(self.driver)
        self.mttb_page = MTTB_Page.MTTB_Page(self.driver)

    """ Переменные для переключения конфига """
    which_environment = 'prod-config'
    # which_environment = 'pp1-config'
    # which_environment = 'pp3-config'

    """В конфиг собранны все ссылки и доступы на портал"""
    configParser = configparser.RawConfigParser()
    prodConfigFilePath = r'C:\MTTB-Autotest\python' \
                         r'\configurationfile'
    configParser.read(prodConfigFilePath)
    lka_login_link = configParser.get(which_environment, 'user_auth1_link')
    userPassword = configParser.get(which_environment, 'userPassword')
    userLogin = configParser.get(which_environment, 'userLogin')
    shopfront_link = configParser.get(which_environment, 'shopfront_link')
    url_path = configParser.get(which_environment, 'user_auth1_link')
    capi_host = configParser.get(which_environment, 'capi_host')
    capi_basic_b64 = configParser.get(which_environment, 'capi_basic_b64')
    capi_basic_b64_for_sms_check_code = configParser.get(
        which_environment, 'capi_basic_b64_for_sms_check_code')
    capi_customer_account_prefix = \
        configParser.get(which_environment, 'capi_customer_account_prefix')
    bapi_host = configParser.get(which_environment, 'bapi_host')
    bapi_proto = configParser.get(which_environment, 'bapi_proto')
    bapi_basic_b64 = configParser.get(which_environment, 'bapi_basic_b64')
    pzv_start_page = configParser.get(which_environment, 'pzv_start_page')
    pzv_login_link = configParser.get(which_environment, 'pzv_login_link')
    pzv_registration_page = configParser.get(which_environment, 'pzv_registration_page')
    pzv_landing_page = configParser.get(which_environment, 'pzv_landing_page')
    mttb_page = configParser.get(which_environment, 'mttb_page')
    pzv_user_login = configParser.get(which_environment, 'pzv_userLogin')
    pzv_website = configParser.get(which_environment, 'pzv_website')
    pzv_managername = configParser.get(which_environment, 'pzv_managername')
    pzv_managerphone = configParser.get(which_environment, 'pzv_managerphone')
    pzv_manageremail = configParser.get(which_environment, 'pzv_manageremail')
    pzv_managerpassword = configParser.get(which_environment, 'pzv_managerpassword')
    pzv_helloworld = configParser.get(which_environment, 'pzv_helloworld')
    pzv_clientphone = configParser.get(which_environment,'pzv_clientphone')
    pzv_dateofissue = configParser.get(which_environment,'pzv_dateofissue')
    pzv_issuedby = configParser.get(which_environment,'pzv_issuedby')
    pzv_passportbirthplace = configParser.get(which_environment,'pzv_passportbirthplace')
    pzv_passportaddress = configParser.get(which_environment,'pzv_passportaddress')
    pzv_passportsurname = configParser.get(which_environment,'pzv_passportsurname')
    pzv_passportname = configParser.get(which_environment,'pzv_passportname')
    pzv_dateofbirth = configParser.get(which_environment,'pzv_dateofbirth')


    def exception_print(self):
        """Вызывается в случае ошибки в тесте.
        Выводит трэйс и закрывает браузер"""
        print("\n!!! ERROR !!!\n")
        print(traceback.format_exc())
        print("======================")
        self.tearDown()

    def test_start(self):
        self.setUp()
        print(inspect.stack()[1][3] + " STARTED \n")

    def test_finish(self):
        self.tearDown()
        print(" \n" + inspect.stack()[1][3] + " PASSED")
        print("=============================")

#     def test_suit(self):
#         print('''
# =====================
# Test Suite has begun
# ---------------------
# ''')
#         self.test001_login()
#         print('''
# ---------------------
# Test Suite has been finished
# =====================
# ''')
#         pass
#
#     def test001_login(self):
#         try:
#             self.test_start()
#             self.login_page.click_log_in_btn()
#             self.login_page.error_msg_email()
#             self.login_page.insert_email(self.userLogin)
#             self.login_page.insert_password(self.userPassword)
#             self.login_page.click_log_in_btn()
#             self.services_page.go_to_action_history_page()
#             self.services_page.click_text_of_service_name('did')
#             # number = self.header.get_account_number()
#             # print(number)
#             # self.header.click_journal_btn()
#             # self.header.click_home_btn()
#             # balance = self.header.get_balance()
#             # print("balance = " + balance)
#             # self.action_history_page.go_to_action_history_page()
#             # self.action_history_page.make_sure_its_action_history_page()
#             # var = self.action_history_page.get_action_history_dateandtime()
#             # print(var)
#             # self.header.click_home_btn()
#             # self.did_free_def_pages.go_to_phone_number_page(number_type_to_go='def')
#             # self.did_free_def_pages.click_buy_number()
#             # self.pagination.check_if_there_is_pagination()
#             # self.pagination.go_to_next_page_if_possible()
#             # self.pagination.go_to_last_page_if_possible()
#             # self.header.log_out()
#             # self.login_page.insert_email(var)
#             self.test_finish()
#         except AttributeError:
#             self.exception_print()
#             pass
#
#     def test002_login(self):
#         pass

    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     SetUpFile().test_suit()
#     # testSuiteRunner = LKApageObject()
#     # print "'__main__2'"
#     # testSuiteRunner.main()
#     pass

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
