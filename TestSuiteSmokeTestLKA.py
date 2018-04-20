# -*- coding: utf-8 -*-
#
import inspect
import time
import unittest
import myjson
import SetUpFile
import Helper


class Config(SetUpFile.SetUpFile):
    """ Здесь хроняться переменные для использования в тестах """
    customer_phone_number = Helper.GenerateCustomerData.generate_customer_phone_number()
    customer_login_email = Helper.GenerateCustomerData.generate_customer_login_email()
    free = None
    did = None
    free_number_monthly_fee = None
    bought_number_free_number_test004 = None
    reserved_status = 'Зарезервирован'
    free_number_tariff = "Базовый 800"
    did_number_tariff = "БизнесIP Минута"
    ip_static_workplace_name = "ip_workplace"
    workplace_name = "workplace name"
    workplace_name_with_lk = "workplace name with lk"
    email_for_workplace = "workplace@auto.test"
    group_name = "group name"
    vpbx_name = "vpbx_name"
    ivr_name = "ivr_name"
    credit_customer_phone_number = Helper.GenerateCustomerData.\
        generate_customer_phone_number()
    credit_customer_email = Helper.GenerateCustomerData.generate_customer_login_email()
    callback_website_adress = "callback_test_website.com"


class TestSuiteSmokeTestLKA(SetUpFile.SetUpFile, unittest.TestCase):

    def test_start_and_login(self):
        print(('\n' + inspect.stack()[1][3]).swapcase())
        self.test_start()
        self.login_lka_steps()

    def login_lka_steps(self, url=Config.lka_login_link,
                        email=Config.customer_login_email,
                        password=Config.customer_password):
        self.login_page.go_to_login(url_to_go=url)
        self.login_page.insert_email(email=email)
        self.login_page.insert_password(password=password)
        self.login_page.click_log_in_btn()

    def test_suit_beginning_prints(self):
        print('''
=====================
Test Suite has begun
---------------------
        ''')
        Helper.DateAndTime.print_current_date_and_time()
        print(Config.customer_login_email)
        print("\n")

    def test_suit(self):
        self.test_suit_beginning_prints()
        # self.test001_registration()
        # self.test030_check_numbers_added_from_shopfront()
        # self.test040_buy_free_number_and_make_sure_it_reserved_then_delete()
        # self.test050_delete_reserved_free_number()
        # self.test060_sign_contract()
        # self.test070_activate_customer()
        # self.test080_generate_and_check_documents()
        # self.test090_change_documents_on_documents_page_and_download_them()
        # self.test100_check_ability_to_turn_voice_record_on()
        # self.test110_creating_different_types_of_workplaces()
        # self.test120_create_group_add_workplace_to_it_and_delete_that_group()
        # self.test130_set_call_forward_schema()
        # self.test140_set_vpbx_schema()
        self.test150_register_credit_customer_and_give_access()
        self.test160_set_credit_limit_for_credit_customer()
        self.test170_turn_voice_record_on()
        self.test180_callback()
        print('''
---------------------
Test Suite has been finished
=====================
''')

    def test001_registration(self):
        self.test_start()
        self.shopfront_quick_signup.go_to_shopfront_page(Config.shopfront_link)
        self.shopfront_quick_signup.go_to_choose_number_page(number_type_page='free')
        Config.free = self.shopfront_quick_signup.buy_any_number_in_list()
        self.shopfront_quick_signup.go_to_choose_number_page(number_type_page='did')
        Config.did = self.shopfront_quick_signup.buy_any_number_in_list()
        self.shopfront_quick_signup.register_with_number(
            number_to_register=Config.customer_phone_number,
            email_to_register=Config.customer_login_email,
            password_to_register=Config.customer_password)
        time.sleep(60)
        self.services_page.make_sure_its_services_page()
        customer_account_number = self.header.get_account_number()
        myjson.update_customer_custom_fields(customer_account_number)
        self.test_finish()

    def test030_check_numbers_added_from_shopfront(self):
        """ Проверка did номара """
        self.test_start_and_login()
        self.did_free_def_pages.go_to_phone_number_page('did')
        self.did_free_def_pages.make_sure_its_phone_number_page('did')
        did_time = self.did_free_def_pages.get_activation_date_of_number(Config.did)
        assert did_time in ''
        did_status = self.did_free_def_pages.get_status_of_number(Config.did)
        assert did_status in Config.reserved_status
        assert self.did_free_def_pages.get_monthly_fee_of_number(Config.did) \
            in self.did_free_def_pages.get_total_charge()
        assert self.did_free_def_pages.get_tariff_of_number(Config.did) \
            in Config.did_number_tariff

        """ Проверка free номара """
        self.did_free_def_pages.go_to_phone_number_page('free')
        self.did_free_def_pages.make_sure_its_phone_number_page('free')
        free_date = self.did_free_def_pages.get_activation_date_of_number(Config.free)
        assert free_date in ''
        free_status = self.did_free_def_pages.get_status_of_number(Config.free)
        assert free_status in Config.reserved_status
        assert self.did_free_def_pages.get_monthly_fee_of_number(Config.free) \
            in self.did_free_def_pages.get_total_charge()
        assert self.did_free_def_pages.get_tariff_of_number(Config.free) \
            in Config.free_number_tariff
        self.test_finish()

    def test040_buy_free_number_and_make_sure_it_reserved_then_delete(self):
        self.test_start_and_login()
        self.home_page.go_to_home_page()
        status = self.home_page.get_current_status()
        self.did_free_def_pages.go_to_phone_number_page('free')
        self.did_free_def_pages.click_buy_number()
        self.pagination.go_to_last_page_if_possible()
        monthly_fee = self.buy_number.get_number_monthly_fee()
        Config.free_number_monthly_fee = monthly_fee
        bought_number = self.buy_number.add_number_to_cart()
        Config.bought_number_free_number_test004 = bought_number
        self.buy_number.buy_number(customer_status=status, sign_agreement=True)
        time.sleep(20)
        self.did_free_def_pages.go_to_phone_number_page('free')
        self.did_free_def_pages.make_sure_its_phone_number_page('free')

        """ Сравнить статус номера """
        assert self.did_free_def_pages.get_status_of_number(bought_number) \
            in Config.reserved_status

        """ Убедиться, что стоимость абон.платы на странице покупки равна 
        стоимости абон.платы на странице 'номера' """
        assert self.did_free_def_pages.get_monthly_fee_of_number(bought_number) \
            in monthly_fee
        self.test_finish()

    def test050_delete_reserved_free_number(self):
        self.test_start_and_login()
        self.did_free_def_pages.go_to_phone_number_page('free')
        self.did_free_def_pages.delete_number_in_list(
            Config.bought_number_free_number_test004)
        time.sleep(25)

        """ Убедиться что после удаления, общая стоимость услуги стала равняться
        стоимости за один номер, купленный с ветрины """
        assert self.did_free_def_pages.get_total_charge() \
            in Config.free_number_monthly_fee
        self.test_finish()

    def test060_sign_contract(self):
        self.test_start_and_login()
        self.home_page.click_sign_contract_btn()
        self.contract_amendment.set_physical_contract_data_on_popup()
        self.header.log_out()
        self.lkm.login_lkm(Config.lkm_url,
                           Config.manager_login, Config.manager_password)
        self.lkm.find_customer_and_sign_contract(
            customer_email_login=Config.customer_login_email)
        self.lkm.log_out_from_lkm()
        self.test_finish()

    def test070_activate_customer(self):
        print(('\n' + inspect.stack()[0][3]).swapcase())
        time.sleep(15)
        myjson.activate_customer(Config.customer_login_email)
        self.test_start_and_login()
        current_status = self.home_page.get_current_status()
        assert current_status in 'Active'
        self.test_finish()

    def test080_generate_and_check_documents(self):
        self.test_start()
        self.lkm.go_to_lkm()
        self.lkm.login_lkm(
            Config.lkm_url, Config.manager_login, Config.manager_password)
        self.lkm.find_customer_and_generate_documents_for_her(
            Config.customer_login_email)
        self.lkm.log_out_from_lkm()
        self.login_lka_steps()
        self.documents_page.go_to_documents_page()
        self.documents_page.make_sure_its_documents_page()
        self.documents_page.download_document()
        self.test_finish()

    def test090_change_documents_on_documents_page_and_download_them(self):
        self.test_start_and_login()
        self.documents_page.go_to_documents_page()
        self.documents_page.make_sure_its_documents_page()
        self.documents_page.change_document()
        self.contract_amendment.make_sure_its_contract_amendment_page()
        print("contract_type is " + self.contract_amendment.findout_contract_type())
        self.contract_amendment.change_physical_contract(wordmark='test009')
        self.home_page.go_to_home_page()
        self.header.click_account_number()
        self.documents_page.make_sure_its_documents_page()
        self.documents_page.download_document(
            name_of_document_to_download='Договор на оказание услуг')
        self.documents_page.make_sure_its_documents_page()
        self.test_finish()

    def test110_creating_different_types_of_workplaces(self):
        """ создание рабочего местоа sip """
        self.test_start_and_login()
        self.workplace_page.go_to_workplace_page()
        self.workplace_page.click_create_new_workplace_btn()
        self.workplace_settings.set_workplace_name(Config.workplace_name)
        self.workplace_settings.set_sip_id()
        self.workplace_settings.set_sip_password()
        self.workplace_settings.save_workplace_form()
        time.sleep(20)

        """ создание рабочего местоа sip c ЛК"""
        self.workplace_page.go_to_workplace_page()
        self.workplace_page.click_create_new_workplace_btn()
        self.workplace_settings.set_workplace_name(Config.workplace_name_with_lk)
        self.workplace_settings.set_sip_id()
        self.workplace_settings.set_sip_password()
        self.workplace_settings.create_lk()
        email_for_workplace = (Helper.get_timestamp() + "@auto.test")
        self.workplace_settings.set_email(email_for_workplace)
        self.workplace_settings.set_internal_number("456")
        self.workplace_settings.set_password()
        self.workplace_settings.set_limit("5000")
        self.workplace_settings.click_fax_checkbox()
        self.workplace_settings.save_workplace_form()
        time.sleep(20)

        """ создание рабочего местоа ip static """
        self.test_start_and_login()
        self.workplace_page.go_to_workplace_page()
        self.workplace_page.click_create_new_workplace_btn()
        self.workplace_settings.create_workplace_with_ip_static(
            udp_or_tcp='tcp',
            workplace_name=Config.ip_static_workplace_name,
            workplace_position='position',
            create_lk=False
        )
        self.workplace_page.go_to_workplace_page()
        time.sleep(20)

        """ удаление рабочего местоа sip """
        self.workplace_page.go_to_workplace_page()
        self.workplace_page.go_to_workplace_settings(Config.workplace_name)
        self.workplace_settings.delete_workplace()
        self.workplace_page.make_sure_there_is_no_such_workplace(
            Config.workplace_name)

        """ удаление рабочего местоа sip c ЛК"""
        self.workplace_page.go_lks(
            workplace_to_go_into_lks=Config.workplace_name_with_lk)
        self.header.log_out()
        self.workplace_page.go_to_workplace_page()
        self.workplace_page.go_to_workplace_settings(Config.workplace_name_with_lk)
        self.workplace_settings.delete_workplace()
        self.workplace_page.make_sure_there_is_no_such_workplace(
            Config.workplace_name_with_lk)

        """ удаление рабочего местоа ip static """
        self.workplace_page.go_to_workplace_settings(
            workplace_name_to_open=Config.ip_static_workplace_name)
        self.workplace_settings.delete_workplace()
        self.workplace_page.make_sure_there_is_no_such_workplace(
            Config.ip_static_workplace_name)

        self.test_finish()

    def test120_create_group_add_workplace_to_it_and_delete_that_group(self):
        """ Создание группы """
        self.test_start_and_login()
        self.group_page.go_to_group_page()
        self.group_page.make_sure_its_group_page()
        self.group_page.click_add_group()
        self.group_page.set_group_name(Config.group_name)
        group_email = (Helper.get_timestamp()) + "@auto.test"
        self.group_page.set_group_email(group_email)
        self.group_page.set_group_internal_number(Helper.get_timestamp()[-0:-4])
        self.group_page.set_sequence(
            sequence_is_random_or_simultaneous_or_order='random')
        self.group_page.set_group_sound()
        self.group_page.click_save_btn()

        """ добавление РМ в группу """
        self.group_page.go_to_group_page()
        self.group_page.add_workplace_to_group("Администратор")

        """ удаление группы """
        self.group_page.go_to_group_page()
        self.group_page.delete_group(Config.group_name)
        self.test_finish()

    def test130_set_call_forward_schema(self):
        """ Создаем группу для добавления в схему """
        group_name_to_add_to_shema = "group_name_to_add_to_shema"
        self.test_start_and_login()
        self.group_page.go_to_group_page()
        self.group_page.make_sure_its_group_page()
        self.group_page.click_add_group()
        self.group_page.set_group_name(group_name_to_add_to_shema)
        group_email = (Helper.get_timestamp()) + "@auto.test"
        self.group_page.set_group_email(group_email)
        self.group_page.set_group_internal_number(Helper.get_timestamp()[-0:-4])
        self.group_page.set_sequence(
            sequence_is_random_or_simultaneous_or_order='random')
        self.group_page.set_group_sound()
        self.group_page.click_save_btn()

        """ Переходим к созданию схемы переадресации """
        self.call_processing_page.go_to_call_processing_page()
        self.call_processing_page.make_sure_its_call_processing_page()
        self.set_call_forwards_and_ivr.set_call_forward_number(
            number_to_set_call_forward_on=Config.did,
            number_to_insert_for_call_forwarding=Config.did)
        self.set_call_forwards_and_ivr.set_call_forward_workplace(
            number_to_set_call_forward_on=Config.did,
            workplace="Администратор")
        self.set_call_forwards_and_ivr.set_call_forward_group(
            number_to_set_call_forward_on=Config.did,
            group_name=group_name_to_add_to_shema)
        self.set_call_forwards_and_ivr.set_call_forward_sip(
            number_to_set_call_forward_on=Config.did,
            login="111",
            domain=Helper.generate_ip_static())
        self.set_call_forwards_and_ivr.set_call_forward_voice_mail(
            number_to_set_call_forward_on=Config.did,
            voicemail_email=(Helper.get_timestamp() + "@auto.test"))
        self.set_call_forwards_and_ivr.set_call_forward_skype(
            number_to_set_call_forward_on=Config.did,
            skype_name_to_insert="test")
        self.call_processing_page.go_to_call_processing_page()
        self.call_processing_page.make_sure_its_call_processing_page()
        self.header.take_a_screenshot_in_base64_format()
        self.test_finish()

    def test140_set_vpbx_schema(self):
        """ установка vpbx_schema and then ivr """
        self.test_start_and_login()
        self.call_processing_page.go_to_call_processing_page()
        self.call_processing_page.make_sure_its_call_processing_page()
        self.set_call_forwards_and_ivr.set_new_vpbx_schema_call_forward(
            number_to_set_vpbx_on=Config.did)
        self.set_call_forwards_and_ivr.click_add_new_call_forward_within_vpbx_schema()
        self.set_call_forwards_and_ivr.set_ivr_within_vpbx_schema(
            set_ivr_name=Config.ivr_name)

        """ Шаги по удалению ivr and then vpbx schema """
        self.call_processing_page.go_to_call_processing_page()
        self.call_processing_page.make_sure_its_call_processing_page()
        self.call_processing_page.open_number_current_call_forward(
            number_to_open=Config.did)
        self.set_call_forwards_and_ivr.delete_ivr(ivr_name_to_delete=Config.ivr_name)
        self.set_call_forwards_and_ivr.delete_vpbx_schema()
        self.call_processing_page.make_sure_its_call_processing_page()
        self.test_finish()

    def test150_register_credit_customer_and_give_access(self):
        self.test_start()
        self.lkm.login_lkm(url=Config.lkm_url, email=Config.manager_login,
                           password=Config.manager_password)
        self.lkm.register_customer_on_lkm(
            customer_type_juridical_or_physical='juridical',
            payment_type_prepayment_or_credit='credit',
            customer_email=Config.credit_customer_email,
            customer_phone_number=Config.credit_customer_phone_number,
            with_package=False,
            buy_did=True,
            buy_free=False,
            buy_mobile=False)
        self.lkm.find_customer_and_give_access_and_login_lka(
            customer_email=Config.credit_customer_email,
            customer_phone_number=Config.credit_customer_phone_number)
        self.home_page.make_sure_its_home_page()
        customer_account_number = self.header.get_account_number()
        myjson.update_customer_custom_fields(customer_account_number)
        self.test_finish()

    def test160_set_credit_limit_for_credit_customer(self):
        self.test_start()
        self.lkm.login_lkm(url=Config.lkm_url,
                           email=Config.manager_login_security,
                           password=Config.manager_password_security)
        self.lkm.find_customer_set_credit_limit_and_activate(
            customer_email=Config.credit_customer_email,
            credit_limit_amount='1500')
        self.test_finish()

    def test170_turn_voice_record_on(self):
        self.test_start_and_login()
        self.voice_record_page.go_to_voice_record_page()
        self.voice_record_page.make_sure_its_voice_record_page()
        self.voice_record_page.turn_record_on_or_off(sign_agreement=False)
        self.voice_record_page.make_sure_its_voice_record_page()
        self.test_finish()

    def test180_callback(self):
        """ Тест кейс только при наличии денег """
        self.test_start_and_login()
        self.callback_services_page.go_to_callback_services_page()
        self.callback_services_page.make_sure_its_callback_services_page()
        self.callback_services_page.add_callback_on_services_page()
        self.callback_page.set_website_address(
            website_adress=Config.callback_website_adress)
        self.callback_page.save_callback()
        self.callback_settings_page.go_to_callback_settings_page()
        self.callback_settings_page.make_sure_its_callback_settings_page()
        self.callback_settings_page.open_callback_settings_popup(
            callback_name=Config.callback_website_adress)
        self.callback_page.geo_targeting(need_to_be_checked=True)
        self.callback_page.go_catch_leave_tab()
        self.callback_page.catch_leave_check(catch_leave_checked=True)
        self.callback_page.go_schedule_tab()
        self.callback_page.set_schedule(
            day_of_week_checked=False)
        self.callback_page.go_text_tab()
        self.callback_page.set_text('1', '2', '3', '4', '5', '6')
        self.callback_page.go_appearance_tab()
        self.callback_page.save_callback()
        self.callback_settings_page.make_sure_its_callback_settings_page()
        self.test_finish()

    def test998_take_screen_shot(self):
        self.header.take_a_screenshot_in_base64_format()

    def test999_delete_customer_in_lkm(self, customer_email_to_delete):
        self.test_start()
        self.lkm.login_lkm(
            Config.lkm_url, Config.manager_login, Config.manager_password)
        self.lkm.delete_customer(customer_email_to_delete)
        self.test_finish()

if __name__ == '__main__':
    try:
        TestSuiteSmokeTestLKA().test_suit()
    except ProcessLookupError:
        TestSuiteSmokeTestLKA().test998_take_screen_shot()
    finally:
        TestSuiteSmokeTestLKA().test999_delete_customer_in_lkm(
            Config.customer_login_email)

# if __name__ == '__main__':
#     unittest.main(
#         # catchbreak=TestSuiteSmokeTestLKA().test999_delete_customer_in_lkm(
#         #     Config.customer_login_email)
#     )
#     # unittest.main(verbosity=2)
