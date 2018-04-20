# -*- coding: utf-8 -*-
#
import inspect
import unittest
import sys
from urllib.parse import urlparse
import time
from selenium.webdriver.common.keys import Keys
import SetUpFile
import init_driver


class ContractAmendment(init_driver.InitDriver):

    title = "Документы > Изменение договора"
    url_path = "/accounting/documents/editContract"
    pageTitleElement = "//div[@class='page_title']/h1"
    navigationBarElement = "//div[@class='lR__dark']/a[@class='lR__it nav lR__it_active'][contains(.,'Документы')]"
    changeContractBtn = "//table['tbl-grey']//a[contains(.,'Изменить договор')]"
    defineAsPhysical = "//*[@id='contractEdit-form']/div[1]/strong[contains(.,'Паспортные данные')]"
    defineAsJuridical = "//*[@id='contractEdit-form']/div[1]/*[contains(.,'Поиск организации')]"
    lastName = ".//*[@id='ContractData_lastName']"
    firstName = ".//*[@id='ContractData_firstName']"
    middleName = ".//*[@id='ContractData_middleName']"
    passportSeries = ".//*[@id='ContractData_passportSeries']"
    passportNumber = ".//*[@id='ContractData_passportNumber']"
    passportIssuedBy = ".//*[@id='ContractData_passportIssuedBy']"
    passportIssueDate = ".//*[@id='ContractData_passportIssueDate']"
    birthDate = ".//*[@id='ContractData_birthDate']"
    birthPlace = ".//*[@id='ContractData_birthPlace']"
    residenceCountry = ".//*[@id='ContractData_residenceCountry']"
    saveBtn = "//a[@class='button-red contract-edit-submit'][text()='Сохранить']"
    searchOrganization = ".//*[@id='yw0_field']"
    equipmentAddressFields = "//label[@for='ContractData_equipmentAddress']/parent::label/textarea"
    signerEmail = ".//*[@id='ContractData_signerEmail']"
    signerPhone = ".//*[@id='ContractData_signerPhone']"
    contact = ".//*[@id='ContractData_contact']"
    contactEmail = ".//*[@id='ContractData_contactEmail']"
    contactPhone = ".//*[@id='ContractData_contactPhone']"
    bankbik = ".//*[@id='ContractData_bik']"
    bankAccount = ".//*[@id='ContractData_bankAccount']"
    bankAccountNumber = "12345678901234567890"
    equipmentAddressFirstPartOfXpath = "//form/div[contains(.,'Индекс, Название улицы, номер дома')]["
    equipmentAddressSecondPartOfXpath = "]//textarea"
    postalAddress = "//*[@id='ContractData_postalAddress_address']"
    continue_btn = "//*[@id='contractRegistration-form']//button[contains(.,'Далее')]"
    close_popup_about_process = "//*[@class='popup__title'][contains(.,'Регистрация договора почти завершена')]" \
                                "/parent::*/parent::*/parent::*//*[@class='popup__close']"

    def go_to_contract_amendment_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_contract_amendment_page(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path + self.url_path)

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            print(inspect.stack()[0][3])
            self.wait_for_element(self.navigationBarElement).click()
            self.wait_for_element(self.changeContractBtn).click()
            time.sleep(3)
            assert self.driver.title in self.title

        """ вызов описанных функций """
        make_sure_its_correct_url()
        # make_sure_its_correct_title()
        pass

    def findout_contract_type(self):
        print(inspect.stack()[0][3])
        """ Возвращает тип клиента juridical или physical """
        try:
            self.wait_for_element(self.defineAsJuridical).click()
            return "juridical"
        except UserWarning:
            self.wait_for_element(self.defineAsPhysical).click()
            return "physical"
        pass

    def fill_all_fields_of_physical_contract_besides_names(self, wordmark="test"):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passportSeries).clear()
        self.wait_for_element(self.passportSeries).send_keys("1234")
        self.wait_for_element(self.passportNumber).clear()
        self.wait_for_element(self.passportNumber).send_keys("123123")
        self.wait_for_element(self.passportIssueDate).click()
        self.wait_for_element(self.passportIssueDate).clear()
        self.wait_for_element(self.passportIssueDate).send_keys("01.01.2016")
        time.sleep(0.2)
        self.wait_for_element(self.passportIssuedBy).click()
        time.sleep(2)
        self.wait_for_element(self.birthDate).click()
        self.wait_for_element(self.birthDate).clear()
        time.sleep(0.1)
        self.wait_for_element(self.birthDate).send_keys("01.01.1980")
        time.sleep(0.2)
        self.wait_for_element(self.passportIssuedBy).click()
        self.wait_for_element(self.passportIssuedBy).clear()
        self.wait_for_element(self.passportIssuedBy).send_keys(wordmark + "_" + "passportIssuedBy")
        self.wait_for_element(self.birthPlace).clear()
        self.wait_for_element(self.birthPlace).send_keys(wordmark + "_" + "birthPlace")
        self.wait_for_element(self.residenceCountry).clear()
        self.wait_for_element(self.residenceCountry).send_keys(wordmark + "_" + "residenceCountry")

    def change_physical_contract(self, wordmark="test"):
        print(inspect.stack()[0][3])
        self.fill_all_fields_of_physical_contract_besides_names(wordmark=wordmark)
        self.wait_for_element(self.saveBtn).click()

    def fill_physical_contract(self, wordmark="test"):
        print(inspect.stack()[0][3])
        wordmark = str(wordmark)
        self.wait_for_element(self.lastName).send_keys(wordmark + "_" + "lastName")
        self.wait_for_element(self.firstName).send_keys(wordmark + "_" + "firstName")
        self.wait_for_element(self.middleName).send_keys(wordmark + "_" + "middleName")
        self.fill_all_fields_of_physical_contract_besides_names(wordmark=wordmark)

    def set_physical_contract_data_on_contract_amendment_page(self, wordmark="test"):
        print(inspect.stack()[0][3])
        self.fill_physical_contract(wordmark=wordmark)
        self.wait_for_element(self.saveBtn).click()

    def set_physical_contract_data_on_popup(self, wordmark="test"):
        print(inspect.stack()[0][3])
        self.fill_physical_contract(wordmark=wordmark)
        self.wait_for_element(self.continue_btn).click()
        self.wait_for_element(self.close_popup_about_process).click()

    def set_juridical_contract_data(self, wordmark="test", company="supermet"):
        print(inspect.stack()[0][3])
        wordmark = str(wordmark)
        self.wait_for_element(self.searchOrganization).click()
        self.wait_for_element(self.searchOrganization).clear()
        self.wait_for_element(self.searchOrganization).send_keys(company)
        self.wait_for_element(self.searchOrganization).send_keys(Keys.DOWN)
        self.wait_for_element(self.searchOrganization).send_keys(Keys.ENTER)
        self.wait_for_element(self.searchOrganization).send_keys(Keys.PAGE_DOWN)
        self.wait_for_element(self.lastName).send_keys(wordmark + "_" + "lastName")
        self.wait_for_element(self.firstName).send_keys(wordmark + "_" + "firstName")
        self.wait_for_element(self.middleName).send_keys(wordmark + "_" + "middleName")
        self.wait_for_element(self.signerEmail).send_keys(wordmark + "@auto.test")
        self.wait_for_element(self.signerPhone).send_keys("+79994448844")
        self.wait_for_element(self.contact).send_keys(wordmark + "_" + "FIO")
        self.wait_for_element(self.contactEmail).send_keys(wordmark + "@" + "contact.email")
        self.wait_for_element(self.bankbik).send_keys("044525225")
        self.wait_for_element(self.bankAccount).send_keys(self.bankAccountNumber)
        self.driver.find_elements_by_xpath(self.equipmentAddressFields).send_keys(wordmark)
        self.wait_for_element(self.postalAddress).clear()
        self.wait_for_element(self.postalAddress).send_keys("мира 2")
        self.wait_for_element(self.postalAddress).send_keys(Keys.DOWN)
        self.wait_for_element(self.postalAddress).send_keys(Keys.ENTER)
        self.wait_for_element(self.saveBtn).click()
