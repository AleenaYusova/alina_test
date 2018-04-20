# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import Helper
import SetUpFile
import init_driver


class DidFreeDefPages(init_driver.InitDriver):

    directory_path = "/services/"
    did_title = "Многоканальный городской номер"
    free_title = "Бесплатный вызов (8-800, 8-804)"
    def_title = "Мобильный номер"
    did_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Многоканальный городской номер')]"
    free_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Бесплатный вызов (8-800, 8-804)')]"
    def_navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Мобильный номер')]"
    buy_number_btn = "//*[@class='button-red add-number nav'][contains(.,'Добавить номер')]"
    first_part_of_xpath = "//a[@class='link-dashed nav'][@number='"
    tariff_second_part_of_xpath = "']/parent::*/parent::div/parent::div/div[2]"
    monthly_fee_second_part_of_xpath = "']/parent::*/parent::div/parent::div/div[3]/b"
    status_second_part_of_xpath = "']/parent::*/parent::div/parent::div/div[4]"
    activation_date_second_part_of_xpath = "']/parent::*/parent::div/parent::div/div[5]"
    delete_btn = "//*[@class='layout__basket-bg-bl delete-button'][@number='"
    delete_confirmation_btn = ".//*[@id='confirm-number-removing-form']//button[contains(.,'Удалить')]"
    cancel_deletion_btn = "']/parent::*/parent::div/parent::div/div[4]/*[contains(.,'Отмена')]"
    cancel_deletion_confirmation_btn = "//button[contains(.,'Отменить удаление')]"
    total_charge = "//td[contains(.,'Всего абонентская плата')]/parent::*//b"

    def go_to_phone_number_page(self, number_type_to_go):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.directory_path + number_type_to_go
        self.driver.get(new_url)
        pass

    def make_sure_its_phone_number_page(self, number_type):
        print(inspect.stack()[0][3])

        def make_sure_its_correct_url():
            """ Проверка правильности пути в url """
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path
                                               + self.directory_path + number_type)
            pass

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            if number_type == "did":
                self.wait_for_element(self.did_navigationBarElement).click()
                time.sleep(3)
                assert self.driver.title in self.did_title
            elif number_type == "free":
                self.wait_for_element(self.free_navigationBarElement).click()
                time.sleep(3)
                assert self.driver.title in self.free_title
            elif number_type == "def":
                self.wait_for_element(self.def_navigationBarElement).click()
                time.sleep(3)
                assert self.driver.title in self.def_title
            else:
                print(AttributeError)
                self.driver.quit()
            pass

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()
        pass

    def click_buy_number(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.buy_number_btn).click()

    def find_number_on_page(self, number_to_fined):
        print(inspect.stack()[0][3])
        number = Helper.GetShortNumber.get_short_number(number_to_fined)
        found_number = self.wait_for_element(self.first_part_of_xpath + str(number) + "']").text
        return found_number

    def get_tariff_of_number(self, number_to_get_tariff_of):
        print(inspect.stack()[0][3])
        number_to_get_tariff_of = Helper.GetShortNumber.get_short_number(number_to_get_tariff_of)
        tariff = self.wait_for_element(self.first_part_of_xpath + str(number_to_get_tariff_of)
                                       + self.tariff_second_part_of_xpath).text
        return tariff

    def get_monthly_fee_of_number(self, number_to_get_monthly_fee_of):
        print(inspect.stack()[0][3])
        number_to_get_monthly_fee_of = Helper.GetShortNumber.get_short_number(number_to_get_monthly_fee_of)
        monthly_fee = self.wait_for_element(self.first_part_of_xpath + str(number_to_get_monthly_fee_of) +
                                                 self.monthly_fee_second_part_of_xpath).text
        monthly_fee = monthly_fee.replace(' ', '')
        return monthly_fee

    def get_status_of_number(self, number_to_get_status_of):
        print(inspect.stack()[0][3])
        number_to_get_status_of = Helper.GetShortNumber.get_short_number(number_to_get_status_of)
        status = self.wait_for_element(self.first_part_of_xpath + str(number_to_get_status_of)
                                       + self.status_second_part_of_xpath).text
        return status

    def get_activation_date_of_number(self, number_activation_date_of):
        print(inspect.stack()[0][3])
        number_activation_date_of = Helper.GetShortNumber.get_short_number(number_activation_date_of)
        activation_date = self.wait_for_element(self.first_part_of_xpath + str(number_activation_date_of) +
                                                self.activation_date_second_part_of_xpath).text
        activation_date = activation_date.replace(' ', '')
        return activation_date

    def delete_number_in_list(self, number_to_delete):
        print(inspect.stack()[0][3])
        number_to_delete = Helper.GetShortNumber.get_short_number(number_to_delete)
        self.wait_for_element(self.delete_btn + str(number_to_delete) + "']").click()
        self.wait_for_element(self.delete_confirmation_btn).click()

    def get_date_of_deferred_deletion(self, number_to_get_date_of):
        print(inspect.stack()[0][3])
        number_to_get_date_of = Helper.GetShortNumber.get_short_number(number_to_get_date_of)
        status = self.wait_for_element(self.first_part_of_xpath + str(number_to_get_date_of)
                                       + self.status_second_part_of_xpath).text
        status = status.replce('Ожидает удаления ', '')
        status = status.replce('Отмена', '')
        status = status.replce(' ', '')
        return status

    def cancel_deletion_of_number_in_list(self, number_cancel_delete_of):
        print(inspect.stack()[0][3])
        number_cancel_delete_of = Helper.GetShortNumber.get_short_number(number_cancel_delete_of)
        self.wait_for_element(self.first_part_of_xpath + str(number_cancel_delete_of) +
                              self.cancel_deletion_btn).click()
        self.wait_for_element(self.cancel_deletion_confirmation_btn).click()

    def get_total_charge(self):
        print(inspect.stack()[0][3])
        total_charge = self.wait_for_element(self.total_charge).text
        total_charge = total_charge.replace(' ', '')
        no_spaces = total_charge.replace(' ', '')
        return no_spaces
