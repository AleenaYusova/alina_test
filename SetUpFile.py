# -*- coding: utf-8 -*-
#
from selenium import webdriver
import AccountingFilter
import ActionHistoryPage
import AdminSettingsPage
import BuyNumber
import CallbackPage
import CallbackServicesPage
import CallbackSettingsPage
import CallProcessingPage
import CLI
import configparser
import ContractAmendment
import DetailedCallsPage
import DidFreeDefPages
import DocumentsPage
import ExpensesPage
import FaxPage
import GroupPage
import Header
import HomePage
import inspect
import JournalCalls
import JournalFilters
import LKM
import Login
import NotificationPage
import Pagination
import PaymentsPage
import ServicesPage
import SetCallForwardsAndIVR
import ShopfrontQuickSignUp
import SIMpage
import sqltestfile
import SupportPage
import traceback
import unittest
import VoiceMailPage
import VoiceRecordPage
import VoIPPpage
import VPBXpage
import VPBXSettings
import WorkplaceCallForwardSchema
import WorkplaceFMCSection
import WorkplacePage
import WorkplaceSettings


class SetUpFile(unittest.TestCase):

    def setUp(self):
        """ Запуск драйвера по умолчанию"""
        self.driver = webdriver.Chrome()
        """ Расширение окна браузера на полный экран"""
        self.driver.maximize_window()
        # self.driver.implicitly_wait(60)
        # """ Переход по URL из конфиг.файла"""
        # self.driver.get(self.url_path)

        """ Присваивание классов страниц """
        self.login_page = Login.Login(self.driver)
        self.header = Header.Header(self.driver)
        self.action_history_page = ActionHistoryPage.ActionHistoryPage(self.driver)
        self.accounting_filter = AccountingFilter.AccountingFilter(self.driver)
        self.admin_settings_page = AdminSettingsPage.AdminSettingsPage(self.driver)
        self.buy_number = BuyNumber.BuyNumber(self.driver)
        self.callback_page = CallbackPage.CallbackPage(self.driver)
        self.callback_services_page = \
            CallbackServicesPage.CallbackServicesPage(self.driver)
        self.callback_settings_page = \
            CallbackSettingsPage.CallbackSettingsPage(self.driver)
        self.cli = CLI.CLI(self.driver)
        self.contract_amendment = ContractAmendment.ContractAmendment(self.driver)
        self.home_page = HomePage.HomePage(self.driver)
        self.call_processing_page = \
            CallProcessingPage.CallProcessingPage(self.driver)
        self.journal_calls = JournalCalls.JournalCalls(self.driver)
        self.journal_filters = JournalFilters.JournalFilters(self.driver)
        self.vpbx_ettings = VPBXSettings.VPBXSettings(self.driver)
        self.did_free_def_pages = DidFreeDefPages.DidFreeDefPages(self.driver)
        self.notification_page = NotificationPage.NotificationPage(self.driver)
        self.pagination = Pagination.Pagination(self.driver)
        self.payments_page = PaymentsPage.PaymentsPage(self.driver)
        self.detailed_calls_page = DetailedCallsPage.DetailedCallsPage(self.driver)
        self.documents_page = DocumentsPage.DocumentsPage(self.driver)
        self.group_page = GroupPage.GroupPage(self.driver)
        self.expenses_page = ExpensesPage.ExpensesPage(self.driver)
        self.services_page = ServicesPage.ServicesPage(self.driver)
        self.voip_page = VoIPPpage.VoIPPpage(self.driver)
        self.support_page = SupportPage.SupportPage(self.driver)
        self.set_call_forwards_and_ivr = SetCallForwardsAndIVR.\
            SetCallForwardsAndIVR(self.driver)
        self.workplace_call_forward_schema = WorkplaceCallForwardSchema.\
            WorkplaceCallForwardSchema(self.driver)
        self.sim_page = SIMpage.SimPage(self.driver)
        self.shopfront_quick_signup = \
            ShopfrontQuickSignUp.ShopfrontQuickSignUp(self.driver)
        self.voice_mail_page = VoiceMailPage.VoiceMailPage(self.driver)
        self.fax_page = FaxPage.FaxPage(self.driver)
        self.voice_record_page = VoiceRecordPage.VoiceRecordPage(self.driver)
        self.vpbx_page = VPBXpage.VpbxPage(self.driver)
        self.workplace_fmc_section = WorkplaceFMCSection.\
            WorkplaceFMCSection(self.driver)
        self.workplace_page = WorkplacePage.WorkplacePage(self.driver)
        self.workplace_settings = WorkplaceSettings.WorkplaceSettings(self.driver)
        self.lkm = LKM.LKM(self.driver)
        self.sql = sqltestfile.Query()

    """ Переменные для переключения конфига """
    # which_environment = 'prod-config'
    # which_environment = 'pp1-config'
    which_environment = 'pp3-config'

    """В конфиг собранны все ссылки и доступы на портал"""
    configParser = configparser.RawConfigParser()
    prodConfigFilePath = r'C:\MTTBPageObjectTestProject\python' \
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
    lkm_url = (configParser.get(which_environment, 'user_auth1_link')
                               + configParser.get(which_environment, 'manager_auth_link'))
    customer_password = configParser.get(which_environment, 'userPassword')
    manager_login = configParser.get(which_environment, 'manager_login')
    manager_password = configParser.get(which_environment, 'manager_password')
    manager_login_security = configParser.get(which_environment, 'manager_login_security')
    manager_password_security = \
        configParser.get(which_environment, 'manager_password_security')

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
