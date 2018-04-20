# -*- coding: utf-8 -*-
#
import inspect
import Helper
import time
from selenium.webdriver.common.keys import Keys
import init_driver
import CallProcessingPage


class SetCallForwardsAndIVR(init_driver.InitDriver):
    """ Класс описывает PopUp 'Настройка переадресации' и настройки схемы и IVR """

    element_in_list = "//*[@id='modal-call-processing']" \
                      "//li[@class='dlist__it call_forwarding_item rule-type' and @type='"
    telephone = "telephone"
    aname = "aname"
    group = "group"
    third_party_sip_id = "third_party_sip_id"
    voicemail = "voicemail"
    skype = "skype"
    vpbx_scheme = "vpbx_scheme"
    ivr = "ivr"
    save_btn = "//input[@type='submit' and @value='Сохранить']"
    select_btn = "//input[@type='submit'][@value='Выбрать']"
    insert_phone_number_field = ".//*[@id='CallForwardToTelephoneRule_param']"
    insert_phone_timout_field = ".//*[@id='CallForwardToTelephoneRule_timeout']"
    select_aname_btn = ".//*[@id='CallForwardToWorkplaceRule_param_select']"
    workplacesfilter_search = ".//*[@id='WorkPlacesFilter_search']"
    workplacesfilter_element = "//div[@id='workplaces-list-container']/div/div[2]"
    callforwardtogrouprule_param_select = ".//*[@id='CallForwardToGroupRule_param_select']"
    groupsfilter_search = ".//*[@id='GroupsFilter_search']"
    groupfilter_element = ".//*[@id='groups-list-container']/div/div[2]"
    login_field = ".//*[@id='CallForwardToAccountRule_login']"
    domain_field = ".//*[@id='CallForwardToAccountRule_domain']"
    sip_timeout = ".//*[@id='CallForwardToAccountRule_timeout']"
    insert_voicemail = ".//*[@id='CallForwardToVoicemailRule_param']"
    voicemail_dropdown = ".//*[@id='select-melodies-styler']"
    voicemail_element_dropdown = ".//*[@id='select-melodies-styler']//li[2]"
    inster_skype = ".//*[@id='CallForwardToSkypeRule_param']"
    skype_timeout_field = ".//*[@id='CallForwardToSkypeRule_timeout']"
    new_schema = "//*[@id='modal-call-processing']/div[3]/a"
    select_schema_in_list = ".//*[@id='modal-call-processing']//ul/li/span[contains(.,'"
    vpbx_schema_name = "//*[@id='item-list-container']//span[@class='Llist__numb scheme-name']"
    insert_ivr_name = ".//*[@id='CallForwardToIvrRule_name']"
    ivr_sound_selection = ".//*[@id='CallForwardToIvrRule_promptName-styler']"
    ivr_sound_element_in_list = ".//*[@id='CallForwardToIvrRule_promptName-styler']//li[2]"
    delete_ivr_first_part = ".//*[@id='item-list-container']//ul[@class='Llist']//a/b[contains(.,'"
    delete_ivr_second_part = "')]/parent::*/parent::*/div/a"
    delete_schema = "//a[@class='link-dashed new-scheme-label delete-scheme']"
    workplace_name_field = ".//*[@id='CallForwardToWorkplaceRule_param_text']"
    group_name_field = ".//*[@id='CallForwardToGroupRule_param_text']"
    add_new_call_forward_within_vpbx_schema_btn = ".//*[@id='item-list-container']" \
                                                  "//div[@class='button-green layout__square-gr']"

    def set_call_forward_number(self, number_to_set_call_forward_on,
                                number_to_insert_for_call_forwarding, timeout=10):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.telephone + "']").click()
        self.wait_for_element(self.insert_phone_number_field).send_keys(str(number_to_insert_for_call_forwarding))
        self.wait_for_element(self.insert_phone_timout_field).clear()
        self.wait_for_element(self.insert_phone_timout_field).send_keys(str(timeout))
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        number_from_field_to_assert = Helper.GetShortNumber.get_short_number(
            self.wait_for_element(self.insert_phone_number_field).get_attribute("value"))
        given_number_to_assert = Helper.GetShortNumber.get_short_number(number=number_to_insert_for_call_forwarding)
        assert given_number_to_assert in number_from_field_to_assert

    def set_call_forward_workplace(self, number_to_set_call_forward_on, workplace):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.aname + "']").click()
        self.wait_for_element(self.select_aname_btn).click()
        self.wait_for_element(self.workplacesfilter_search).send_keys(str(workplace))
        self.wait_for_element(self.workplacesfilter_search).send_keys(Keys.ENTER)
        self.wait_for_element(self.workplacesfilter_element).click()
        self.wait_for_element(self.select_btn).click()
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        workplace_name_from_field_to_assert = self.driver.find_element_by_xpath(
            self.workplace_name_field).get_attribute("value")
        assert str(workplace_name_from_field_to_assert.encode("utf-8")) in str(workplace.encode("utf-8"))

    def set_call_forward_group(self, number_to_set_call_forward_on, group_name):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.group + "']").click()
        self.wait_for_element(self.callforwardtogrouprule_param_select).click()
        self.wait_for_element(self.groupsfilter_search).send_keys(str(group_name))
        self.wait_for_element(self.groupfilter_element).click()
        self.wait_for_element(self.select_btn).click()
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        group_name_from_field_to_assert = self.driver.find_element_by_xpath(
            self.group_name_field).get_attribute("value")
        assert str(group_name_from_field_to_assert.encode("utf-8")) in str(group_name.encode("utf-8"))

    def set_call_forward_sip(self, number_to_set_call_forward_on, login, domain, timeout=10):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.third_party_sip_id + "']").click()
        self.wait_for_element(self.login_field).send_keys(str(login))
        self.wait_for_element(self.domain_field).send_keys(str(domain))
        self.wait_for_element(self.sip_timeout).clear()
        self.wait_for_element(self.sip_timeout).send_keys(str(timeout))
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        assert str(self.wait_for_element(self.login_field).get_attribute("value").encode("utf-8")) \
               in str(login.encode("utf-8"))
        assert self.wait_for_element(self.domain_field).get_attribute("value") \
               in str(domain.encode("utf-8"))
        assert self.wait_for_element(self.sip_timeout).get_attribute("value") \
               in str(timeout)

    def set_call_forward_voice_mail(self, number_to_set_call_forward_on, voicemail_email):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.voicemail + "']").click()
        self.wait_for_element(self.insert_voicemail).send_keys(str(voicemail_email))
        self.wait_for_element(self.voicemail_dropdown).click()
        self.wait_for_element(self.voicemail_element_dropdown).click()
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        assert str(self.driver.find_element_by_xpath(self.insert_voicemail).get_attribute("value").encode("utf-8")) \
               in str(voicemail_email.encode("utf-8"))

    def set_call_forward_skype(self, number_to_set_call_forward_on, skype_name_to_insert, skype_timeout=10):
        """ steps to set call forwarding """
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_call_forward_on)
        self.wait_for_element(self.element_in_list + self.skype + "']").click()
        self.wait_for_element(self.inster_skype).send_keys(str(skype_name_to_insert))
        self.wait_for_element(self.skype_timeout_field).clear()
        self.wait_for_element(self.skype_timeout_field).send_keys(str(skype_timeout))
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

        """ steps to make sure this particular call forwarding was set correctly """
        CallProcessingPage.CallProcessingPage(self.driver).open_number_current_call_forward(
            number_to_open=number_to_set_call_forward_on)
        assert str(self.wait_for_element(self.inster_skype).get_attribute("value")) \
               in str(skype_name_to_insert)

    def set_new_vpbx_schema_call_forward(self, number_to_set_vpbx_on):
        print("\n" + inspect.stack()[0][3])
        CallProcessingPage.CallProcessingPage(self.driver).add_call_forward(number=number_to_set_vpbx_on)
        self.wait_for_element(self.element_in_list + self.vpbx_scheme + "']").click()
        self.wait_for_element(self.new_schema).click()
        time.sleep(8)

    def select_vpbx_schema_among_created_in_list_to_set_call_forward(self, ivr_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.element_in_list + self.vpbx_scheme + "']").click()
        self.wait_for_element(self.select_schema_in_list + str(ivr_name) + "')]").click()

    def set_vpbx_schema_name(self, name_to_set):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.vpbx_schema_name).click()
        # self.driver.find_element_by_xpath(self.vpbx_schema_name).send_kays(Keys.CLEAR)
        self.driver.find_element_by_xpath(self.vpbx_schema_name).send_keys(str(name_to_set))
        self.driver.find_element_by_xpath("html/body").click()

    def click_add_new_call_forward_within_vpbx_schema(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.add_new_call_forward_within_vpbx_schema_btn).click()

    def set_ivr_within_vpbx_schema(self, set_ivr_name):
        """ Находясь в настройках VPBX схемы, добавить переадресацию
        'На голосовое меню или голосовое сообщение' == 'IVR' """
        print(inspect.stack()[0][3])
        self.wait_for_element(self.element_in_list + self.ivr + "']").click()
        self.wait_for_element(self.insert_ivr_name).send_keys(str(set_ivr_name))
        self.wait_for_element(self.ivr_sound_selection).click()
        self.wait_for_element(self.ivr_sound_element_in_list).click()
        self.wait_for_element(self.save_btn).click()
        time.sleep(10)

    def delete_ivr(self, ivr_name_to_delete):
        self.wait_for_element(self.delete_ivr_first_part + str(ivr_name_to_delete) +
                              self.delete_ivr_second_part).click()
        time.sleep(10)

    def delete_vpbx_schema(self):
        self.wait_for_element(self.delete_schema).click()
        time.sleep(10)
