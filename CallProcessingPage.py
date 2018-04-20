# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
from selenium.webdriver.common.keys import Keys
import Helper
import SetUpFile
import init_driver


class CallProcessingPage(init_driver.InitDriver):

    url_path = "/settings/callProcessing"
    title = "Входящая связь"
    pageTitleElement = "//div[@class='page_title']/h1"
    navigationBarElement = "//div[@class='lR__dark']/a[contains(.,'Входящая связь')]"
    numberTypeFilterSelecor = ".//*[@id='CallProcessingFilter_town-styler']//div[@class='jq-selectbox__trigger']"
    numberTypeFilterSelecorList = "/parent::div/parent::span//ul/li[contains(.,'"
    searchNumberField = ".//*[@id='CallProcessingFilter_mask']"
    checkboxToSetCallForwardFirstPartOfXpath = ".//*[@id='"
    checkboxToSetCallForwardSecondPartOfXpath = "']/div[1]/span"
    callForwardBtn = "//div[@id='list-container']//*[@class='link-dashed strong call-forwarding-edit-batch']"
    blackListBtnFirstPartOfXpath = ".//*[@id='"
    blackListBtnSecondPartOfXpath = "']/div[4]/*"
    blackListField = ".//*[@id='BlackList_rejectMasks']"
    sevaBlackListPopUpBtn = "//input[@type='submit' AND @value='Сохранить']"
    check_box_on_number_first_part_of_xpath = "//a[@number='"
    check_box_on_number_second_part_of_xpath = "']/parent::*/parent::*/parent::*/" \
                                               "/*[@class='jq-checkbox smpl-checkbox call-processing-item-checkbox']"
    set_call_forward_btn = ".//*[@id='list-container']//a[contains(.,'Переадресация')]"
    open_its_current_call_forward_btn_first_part_of_xpath = "//*[@id='"
    open_its_current_call_forward_btn_second_part_of_xpath = "']/div[3]/div/*"

    def go_to_call_processing_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_call_processing_page(self):
        print(inspect.stack()[0][3])
        # TO DO https://jira.mtt.ru:8443/browse/MTTBPORTAL-5552
        self.wait_for_element(self.navigationBarElement).click()
        time.sleep(3)

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path + self.url_path)

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            print(inspect.stack()[0][3])
            assert self.driver.title in self.title

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()

    def number_type_filter(self, number_type):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.numberTypeFilterSelecor).click()
        self.wait_for_element(self.numberTypeFilterSelecor + str(number_type) +
                              self.numberTypeFilterSelecorList + "')]").click()
        pass

    def search_number(self, number):
        print(inspect.stack()[0][3])
        Helper.GetShortNumber.get_short_number(number=number)
        self.wait_for_element(self.searchNumberField).clear()
        self.wait_for_element(self.searchNumberField).send_keys(number)
        self.wait_for_element(self.searchNumberField).send_keys(Keys.ENTER)

    def open_number_current_call_forward(self, number_to_open):
        print(inspect.stack()[0][3])
        number_to_open = Helper.GetShortNumber.get_short_number(number=number_to_open)
        self.wait_for_element(self.open_its_current_call_forward_btn_first_part_of_xpath + str(number_to_open)
                              + self.open_its_current_call_forward_btn_second_part_of_xpath).click()

    def set_call_forward_on_number(self, number):
        print(inspect.stack()[0][3])
        self.search_number(number)
        number = Helper.GetShortNumber.get_short_number(number)
        self.wait_for_element(self.checkboxToSetCallForwardFirstPartOfXpath + str(number) +
                              self.checkboxToSetCallForwardSecondPartOfXpath).click()
        self.wait_for_element(self.callForwardBtn).click()
        pass

    def set_black_list(self, number_to_apply_black_list, black_number):
        print(inspect.stack()[0][3])
        self.search_number(number_to_apply_black_list)
        number = Helper.GetShortNumber.get_short_number(number_to_apply_black_list)
        self.wait_for_element(self.blackListBtnFirstPartOfXpath + str(number) +
                              self.blackListBtnSecondPartOfXpath).click()
        self.wait_for_element(self.callForwardBtn).click()
        self.wait_for_element(self.blackListField).send_keys(black_number)
        self.wait_for_element(self.blackListField).send_keys(Keys.ENTER)
        self.wait_for_element(self.sevaBlackListPopUpBtn).click()
        pass

    def add_call_forward(self, number):
        print(inspect.stack()[0][3])
        self.go_to_call_processing_page()
        number = Helper.GetShortNumber.get_short_number(number=number)
        xpath = (self.check_box_on_number_first_part_of_xpath +
                              str(number) + self.check_box_on_number_second_part_of_xpath)
        print(xpath)
        self.wait_for_element(xpath).click()
        self.wait_for_element(self.set_call_forward_btn).click()
