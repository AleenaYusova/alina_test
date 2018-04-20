# -*- coding: utf-8 -*-
#
import inspect
import time
import unittest
import requests
import json
import myjson
import SetUpFile
import Helper
import pyperclip


class Config(SetUpFile.SetUpFile):
    """ Здесь хранятся переменные для использования в тестах """
    customer_phone_number = Helper.GenerateCustomerData.generate_customer_phone_number()
    customer_login_email = Helper.GenerateCustomerData.generate_customer_login_email()
    pzv_customer_phone_number = Helper.GenerateCustomerData.generate_customer_phone_number()
    pzv_customer_login_email = "pzv" + Helper.GenerateCustomerData.generate_customer_login_email()
    pzv_managerlogin = "pzv_manager"+ Helper.GenerateCustomerData.generate_customer_login_email()
    passport_series = Helper.GenerateCustomerData.generate_passport_series()
    passport_number = Helper.GenerateCustomerData.generate_passport_number()



class TestSuiteSmokeTestLKA(SetUpFile.SetUpFile, unittest.TestCase):

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
        self.test200_pozvonim_registration()
        self.test201_pozvonim_landing_page()
        # self.test202_pozvonim_main_page()
        # self.login_pzv_steps()
        # self.test203_mttb_page()
        # self.delete_customer()

    

            #         print('''
# ---------------------
# Test Suite has been finished
# =====================
# ''')

    def test200_pozvonim_registration(self):
        self.test_start()
        self.pozvonim_start_page.go_to_pzv_start_page(url_to_go=Config.pzv_start_page)
        self.pozvonim_start_page.click_log_in_btn_registration()
        self.pozvonim_registration_page.insert_phone(phone=Config.pzv_customer_phone_number)
        self.pozvonim_registration_page.insert_email(email=Config.pzv_customer_login_email)
        self.pozvonim_registration_page.insert_password(password=Config.userPassword)
        self.pozvonim_registration_page.click_accept_offer()
        self.pozvonim_registration_page.click_log_in_btn()
        self.pozvonim_registration_page.sms_check_code(number_to_register=Config.pzv_customer_phone_number)
        self.pozvonim_registration_page.profile_btn_click()
        self.pozvonim_registration_page.refresh_page()
        self.pozvonim_registration_page.click_profile_btn()
        self.pozvonim_registration_page.insert_passport_series(passport_series=Config.passport_series)
        self.pozvonim_registration_page.insert_passport_number(passport_number=Config.passport_number)
        self.pozvonim_registration_page.insert_date_of_issue(date_of_issue=Config.pzv_dateofissue)
        self.pozvonim_registration_page.insert_issued_by(issued_by=Config.pzv_issuedby)
        self.pozvonim_registration_page.insert_passport_birth_place(passport_birth_place=Config.pzv_passportbirthplace)
        self.pozvonim_registration_page.insert_passport_address(passport_address=Config.pzv_passportaddress)
        self.pozvonim_registration_page.insert_passport_surname(passport_surname=Config.pzv_passportsurname)
        self.pozvonim_registration_page.insert_passport_name(passport_name=Config.pzv_passportname)
        self.pozvonim_registration_page.insert_date_of_birth(date_of_birth=Config.pzv_dateofbirth)
        self.pozvonim_registration_page.click_save_btn()
        self.pozvonim_registration_page.click_pzv_signcontract_btn()
        self.mttb_page.click_mttb_save_btn()
        self.mttb_page.click_mttb_services_btn()
        self.mttb_page.click_mttb_web_widgets_btn()
        self.mttb_page.click_mttb_to_plug_ww_btn()
        self.pozvonim_registration_page.click_web_widget_btn()
        self.pozvonim_registration_page.click_addproject_btn()
        self.pozvonim_registration_page.select_webwidgets(callback=None, chat='chat', feedback='feedback',
                                                   herdinstinct='herdinstinct')
        self.pozvonim_registration_page.insert_website(website=Config.pzv_website)
        self.pozvonim_registration_page.click_success_btn()
        self.pozvonim_registration_page.click_managers_btn()
        self.pozvonim_registration_page.click_one_free_operator_btn()
        self.pozvonim_registration_page.click_try_free_btn()
        self.pozvonim_registration_page.click_addmanager_btn()
        self.pozvonim_registration_page.click_create_new_operator_btn()
        self.pozvonim_registration_page.insert_manager_name(managername=Config.pzv_managername)
        self.pozvonim_registration_page.insert_manager_phone(managerphone=Config.pzv_managerphone)
        self.pozvonim_registration_page.insert_manager_email(manageremail=Config.pzv_manageremail)
        self.pozvonim_registration_page.insert_manager_login(managerlogin=Config.pzv_managerlogin)
        self.pozvonim_registration_page.insert_manager_password(managerpassword=Config.pzv_managerpassword)
        self.pozvonim_registration_page.click_checkbox_access_callback()
        self.pozvonim_registration_page.click_checkbox_access_premium()
        self.pozvonim_registration_page.click_create_manager_btn()
        self.pozvonim_registration_page.click_web_widget_btn()
        self.pozvonim_registration_page.click_premium_free_btn()
        self.pozvonim_registration_page.click_demo_callback_free_btn()
        self.pozvonim_registration_page.click_set_widget()
        self.pozvonim_registration_page.click_code_for_site()
        self.pozvonim_registration_page.click_copy_code_for_site()
        self.pozvonim_registration_page.click_landing_btn()

        # self.pozvonim_login_page.click_addplaces_btn()
        # self.pozvonim_login_page.click_operators_btn()
        # self.pozvonim_login_page.click_pay_for_places_btn()
        time.sleep(10)
        self.test_finish()

    def test201_pozvonim_landing_page(self):
        self.test_start()
        self.pozvonim_landing_page.go_to_pzv_landing_page(url_to_go=Config.pzv_landing_page)
        self.pozvonim_landing_page.click_landing_site()
        self.pozvonim_landing_page.click_save_changes()
        self.pozvonim_landing_page.refresh_page1()
        self.pozvonim_landing_page.click_chat_btn()
        self.pozvonim_landing_page.insert_helloworld(helloworld=Config.pzv_helloworld)
        self.pozvonim_landing_page.click_enter_btn()
        self.pozvonim_landing_page.click_callback_btn()
        self.pozvonim_landing_page.insert_clientphone(clientphone=Config.pzv_clientphone)
        self.pozvonim_landing_page.click_waiting_for_call_btn()
        time.sleep(10)

    def test202_pozvonim_main_page(self):
        self.test_start()
        self.pozvonim_main_page.go_to_pzv_main_page(url_to_go=Config.pzv_main_page)
        self.pozvonim_main_page.click_profile_btn()
        time.sleep(10)

    def login_pzv_steps(self):
        self.test_start()
        self.pozvonim_start_page.go_to_pzv_start_page(url_to_go=Config.pzv_start_page)
        self.pozvonim_start_page.click_log_in_btn_enter()
        self.pozvonim_login_page.insert_email(email=Config.pzv_user_login)
        self.pozvonim_login_page.insert_password(password=Config.userPassword)
        self.pozvonim_login_page.click_log_in_btn()
        self.pozvonim_login_page.click_profile_btn()
        # self.pozvonim_login_page.insert_passport_series(passport_series=Config.passport_series)
        # self.pozvonim_login_page.insert_passport_number(passport_number=Config.passport_number)
        # self.pozvonim_login_page.insert_date_of_issue(date_of_issue=Config.pzv_dateofissue)
        # self.pozvonim_login_page.insert_issued_by(issued_by=Config.pzv_issuedby)
        # self.pozvonim_login_page.insert_passport_birth_place(passport_birth_place=Config.pzv_passportbirthplace)
        # self.pozvonim_login_page.insert_passport_address(passport_address=Config.pzv_passportaddress)
        # self.pozvonim_login_page.insert_passport_surname(passport_surname=Config.pzv_passportsurname)
        # self.pozvonim_login_page.insert_passport_name(passport_name=Config.pzv_passportname)
        # self.pozvonim_login_page.insert_date_of_birth(date_of_birth=Config.pzv_dateofbirth)
        # self.pozvonim_login_page.click_save_btn()
        # self.pozvonim_login_page.click_pzv_signcontract_btn()
        self.mttb_page.click_mttb_save_btn()
        self.mttb_page.click_mttb_services_btn()
        self.mttb_page.click_mttb_web_widgets_btn()
        self.mttb_page.click_mttb_to_plug_ww_btn()
        self.pozvonim_login_page.update_customer_custom_fields()
        # self.pozvonim_login_page.click_web_widget_btn()
        # self.pozvonim_login_page.click_addproject_btn()
        # self.pozvonim_login_page.select_webwidgets(callback=None, chat='chat', feedback='feedback', herdinstinct='herdinstinct')
        # self.pozvonim_login_page.insert_website(website=Config.pzv_website)
        # self.pozvonim_login_page.click_success_btn()
        # self.pozvonim_login_page.click_managers_btn()
        # self.pozvonim_login_page.click_addmanager_btn()
        # self.pozvonim_login_page.click_create_new_operator_btn()
        # self.pozvonim_login_page.insert_manager_name(managername=Config.pzv_managername)
        # self.pozvonim_login_page.insert_manager_phone(managerphone=Config.pzv_managerphone)
        # self.pozvonim_login_page.insert_manager_email(manageremail=Config.pzv_manageremail)
        # self.pozvonim_login_page.insert_manager_login(managerlogin=Config.pzv_managerlogin)
        # self.pozvonim_login_page.insert_manager_password(managerpassword=Config.pzv_managerpassword)
        # self.pozvonim_login_page.click_checkbox_access_callback()
        # self.pozvonim_login_page.click_checkbox_access_premium()
        # self.pozvonim_login_page.click_create_manager_btn()
        # self.pozvonim_login_page.click_addplaces_btn()
        # self.pozvonim_login_page.click_operators_btn()
        # self.pozvonim_login_page.click_pay_for_places_btn()
        # self.pozvonim_login_page.click_to_sign_btn()
        time.sleep(10)
        self.test_finish()

    def test203_mttb_page(self):
        self.test_start()
        self.mttb_page.go_to_mttb_page(url_to_go=Config.mttb_page)
        self.mttb_page.click_mttb_save_btn()
        time.sleep(10)


    def delete_customer(pzv_customer_login_email):
        print(inspect.stack()[0][3])
        # url = "http://172.16.104.159:88/api/v1/customer"
        # host = "bapi.preprod.dmz.mtt.ru" # preprod
        # host = "172.16.104.159:88" # prod
        proto = Config().bapi_proto
        host = Config().bapi_host
        basic_b64 = Config().bapi_basic_b64
        url = proto + "://" + host + "/api/v1/customer"
        headers = {'content-type': 'application/json',
                   'Authorization': 'Basic ' + basic_b64}
        print(url)
        print(headers)

        payload = {
            "id": "1",
            "jsonrpc": "2.0",
            "method": "makeContractTermination",
            "params":
                {
                    "customer_login": "pzv_customer_login_email",
                    "delete_force": "true"
                }
        }
        print(payload)
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()
        print(response)
        assert response["result"] == {
            "success": 1
        }
        assert response["jsonrpc"]
        assert response["id"] is '1'



if __name__ == '__main__':
    try:
        TestSuiteSmokeTestLKA().test_suit()
    except ProcessLookupError:
        TestSuiteSmokeTestLKA().take_screen_shot()
    finally:
        print("TEST ENDED")


