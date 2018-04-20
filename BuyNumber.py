# -*- coding: utf-8 -*-
#
import inspect
import traceback
import unittest
import sys
from selenium.webdriver.common.keys import Keys
import init_driver
import HomePage


class BuyNumber(init_driver.InitDriver):

    numberFromTheFirstLine = "//div[@class='numbers-content']//tr[2]/td[1]"
    searchField = ".//*[@id='mask']"
    addToCartBtn = "//div[@class='numbers-content']//tr[2]/td[5]/a"
    firstPartOfXpathNumberInCart = "//div[@class='cart-sidebar']//td[contains(.,'"
    popUpNumberIsNotAvailable = "//div[@id='message-dialog']//span[contains(.,'Не удалось добавить номер')]"
    popUpNumberIsNotAvailableOKbtn = "//span[@class='ui-button-text'][text()='OK']"
    activationFee = "//div[@class='numbers-content']//tr[2]/td[3]/b"
    monthlyFee = "//div[@class='numbers-content']//tr[2]/td[3]/b"
    mgp = "//div[@class='numbers-content']//tr[2]/td[4]/b"
    totalActivationFee = "//div[@class='cart-sidebar']//div[@class='cart-sidebar-total-row']" \
                         "/div[contains(.,'Подключение:')]/parent::div/div/b"
    totalMonthlyFee = "//div[@class='cart-sidebar']//div[@class='cart-sidebar-total-row']" \
                      "/div[contains(.,'Абон. плата:')]/parent::div/div/b"
    deleteNumberFromCartBtn = "//div[@class='cart-sidebar']//a[@item-id='"
    buyBtn = "//div[@class='cart-sidebar']//button[text()='Купить']"
    confirmationPopUpYesBtn = "//div[@class='ui-dialog-buttonset']//button/*[text()='Да']"
    equipmentAddress = ".//*[@id='ContractData_equipmentAddress_moscow']"
    equipmentAddressSaveBtn = ".//*[@id='equipmentAddress-form']//button[@class='button-red floatR " \
                              "equipment-address-save']"
    signAgreementBtn = "//div[contains(.,'Подписание документов')]//button/*[text()='Подписать']"
    notSignAgreementBtn = "//div[contains(.,'Подписание документов')]//button/*[text()='Отмена']"

    def get_number_from_list(self):
        print(inspect.stack()[0][3])
        number = self.wait_for_element(self.numberFromTheFirstLine).text
        return number

    def search_number(self, number_to_search):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.searchField).send_keys(number_to_search)
        self.wait_for_element(self.searchField).send_keys(Keys.ENTER)

    def add_number_to_cart(self):
        print(inspect.stack()[0][3])
        number = self.get_number_from_list()
        self.wait_for_element(self.addToCartBtn).click()
        return number

    def get_number_activation_fee(self):
        print(inspect.stack()[0][3])
        activation_fee = self.wait_for_element(self.activationFee).text
        return activation_fee
        pass

    def get_number_monthly_fee(self):
        print(inspect.stack()[0][3])
        monthly_fee = self.wait_for_element(self.monthlyFee).text
        no_spaces = monthly_fee.replace(' ', '')
        no_spaces = no_spaces.replace(' ', '')
        return no_spaces

    def get_number_mgp(self):
        print(inspect.stack()[0][3])
        number_mgp = self.wait_for_element(self.mgp).text
        return number_mgp
        pass

    def get_total_activation_fee(self):
        print(inspect.stack()[0][3])
        total_activation_fee = self.wait_for_element(self.activationFee).text
        return total_activation_fee
        pass

    def get_total_monthly_fee(self):
        print(inspect.stack()[0][3])
        total_monthly_fee = self.wait_for_element(self.totalMonthlyFee).text
        return total_monthly_fee
        pass

    def delete_number_from_cart(self, number_to_delete):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.deleteNumberFromCartBtn + number_to_delete + "']").click()
        self.element_is_not_present(self, self.deleteNumberFromCartBtn + number_to_delete + "']")
        pass

    def buy_number(self, customer_status, sign_agreement=True):
        """ Необходимо передать статус кастомера
        customer_status = self.home_page.get_current_status() """
        print(inspect.stack()[0][3])
        self.wait_for_element(self.buyBtn).click()
        if customer_status is 'Test':
            self.wait_for_element(self.confirmationPopUpYesBtn).click()
            return
        # TO DO
        # elif customer_status is 'Активен':
        else:
            self.wait_for_element(self.confirmationPopUpYesBtn).click()
            self.wait_for_element(self.equipmentAddress).send_keys("test adress")
            self.wait_for_element(self.equipmentAddressSaveBtn).click()
            if sign_agreement is True:
                self.wait_for_element(self.signAgreementBtn).click()
                return
            elif sign_agreement is False:
                self.wait_for_element(self.notSignAgreementBtn).click()
                return
            else:
                print(traceback.format_exc())
                return


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
