# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver
import SIMPageOrderPopUp


class SimPage(init_driver.InitDriver):

    url_path = "/services/sim"
    title = "SIM-карта"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'SIM-карта')]"
    export_sim = "//a[@class='link-dashed action-export-to-excel']"
    sim_wp_name_in_table = ".//*[@id='item-list-container']//td[1][contains(.,'"
    tariff_xpath = "')]/parent::*/td[2]"
    monthly_fee_xpath = "')]/parent::*/td[3]/b"
    status_xpath = "')]/parent::*/td[4]"
    activation_date_xpath = "')]/parent::*/td[5]"
    total_charge_xpath = "//td[contains(.,' Всего абонентская плата')]/parent::*//b"
    order_sim_btn = "//input[@class='button-red action-order']"
    region_delivery_dropdown = ".//*[@id='OrderSimRegistration_regionDelivery-styler']"
    region_delivery_list = ".//*[@id='OrderSimRegistration_regionDelivery-styler']//li[contains(.,'"
    count_sim_dropdown = ".//*[@id='OrderSimRegistration_countSim-styler']"
    count_sim_list = ".//*[@id='OrderSimRegistration_countSim-styler']//li[text()='"
    continue_btn = "//button[contains(.,'Далее')]"
    type_delivery = ".//*[@id='ms_deliverytype_todoor']"
    delivery_free_btn_in_list_of_companies = ".//*[@id='ms_todoors']//*[@class='cw-button'][contains(.,'беспл.')]"
    pickup_type = ".//*[@id='ms_deliverytype_pickup']"
    pickup_click_any_company_in_list = ".//*[@id='ms_pickups']//*[@data-ms-pickuppoint-id]"
    pickup_click_chose_btn = "//div[@class='delivery-point-footer']//*[contains(.,'Выбрать')]"
    activate_sim_btn = "//*[@class='button-red action-activate']"
    activate_sim_chose_wp_dropdown = ".//*[@id='SimProductActivate_listPlace-styler']"
    activate_sim_chose_in_list = ".//*[@id='SimProductActivate_listPlace-styler']//li[contains(.,'"
    generate_code_btn = "//button[contains(.,'Сгенерировать код')]"
    code = "//div[@class='code sim-generated-code_value'][text()]"
    popup_activation_ok_btn = ".//*[@id='modal-select-options']" \
                              "//button[@class='button-red button-red_float_right activate-ok w160']"
    popup_activation_cancel_btn = ".//*[@id='modal-select-options']" \
                                  "//button[@class='button-red button-red_float_right activate-cancel w160']"

    def go_to_sim_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_sim_page(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            assert self.driver.current_url in (SetUpFile.SetUpFile.url_path + self.url_path)
            pass

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            self.wait_for_element(self.navigationBarElement).click()
            time.sleep(3)
            assert self.driver.title in self.title
            pass

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()

    def export_sim_to_excel(self):
        self.wait_for_element(self.export_sim).click()
        self.make_sure_its_sim_page()
        pass

    def click_sim_in_list(self, sim_name_to_click):
        self.wait_for_element(self.sim_wp_name_in_table + str(sim_name_to_click) + "')]").click()
        pass

    def get_sim_tariff(self, name_of_wp_sim_to_get_tariff_of):
        tariff = self.wait_for_element(self.sim_wp_name_in_table + str(name_of_wp_sim_to_get_tariff_of) +
                                       self.tariff_xpath).text
        return tariff
        pass

    def get_sim_monthly_fee(self, name_of_wp_sim_to_get_monthly_fee_of):
        monthly_fee = self.wait_for_element(self.sim_wp_name_in_table + str(name_of_wp_sim_to_get_monthly_fee_of) +
                                            self.monthly_fee_xpath).text
        return monthly_fee
        pass

    def get_sim_status(self, name_of_wp_sim_to_get_status_of):
        status = self.wait_for_element(self.sim_wp_name_in_table + str(name_of_wp_sim_to_get_status_of) +
                                       self.status_xpath).text
        return status
        pass

    def get_activation_date(self, name_of_wp_sim_to_get_activation_date):
        activation_date = self.wait_for_element(self.sim_wp_name_in_table +
                                                str(name_of_wp_sim_to_get_activation_date) +
                                                self.activation_date_xpath).text
        return activation_date
        pass

    def get_total_charge(self):
        total_charge = self.wait_for_element(self.total_charge_xpath).text
        return total_charge
        pass

    def order_sim(self, region, amount_of_sim_cards, pickup_or_delivery):
        """
        Функция, выполняет ряд шагов по заказу sim карты, до перехода на PopUp для заполнения данных.
        Для заполнения данных вызваются методы класса SIMPageOrderPopUp.
        :param region: передается в формате 'Москва', 'Санкт-Петербург', 'Московская область', 'Ленинградская область'
        :param amount_of_sim_cards: целое число от 1 до 30
        :param pickup_or_delivery: передается тип доставки 'pickup' == Самовывозом или 'delivery' == Курьером
        """
        self.wait_for_element(self.order_sim_btn).click()
        self.wait_for_element(self.region_delivery_list + str(region) + "')]").click()
        self.wait_for_element(self.count_sim_dropdown).click()
        amount = int(amount_of_sim_cards)
        self.wait_for_element(self.count_sim_list + str(amount) + "']").click()
        self.wait_for_element(self.continue_btn).click()

        if pickup_or_delivery is 'pickup':
            self.wait_for_element(self.pickup_type).click()
            self.wait_for_element(self.pickup_click_any_company_in_list).click()
            time.sleep(5)
            self.wait_for_element(self.pickup_click_chose_btn).click()
            SIMPageOrderPopUp.SIMPageOrderPopUp(self.driver).assert_in_region_and_sim_amount(
                region_should_be=region,
                amount_of_sim_cards_should_be=amount_of_sim_cards
            )
            SIMPageOrderPopUp.SIMPageOrderPopUp(self.driver).order_sim_popup_for_pickup()

        elif pickup_or_delivery is 'delivery':
            self.wait_for_element(self.type_delivery).click()
            self.wait_for_element(self.delivery_free_btn_in_list_of_companies).click()
            SIMPageOrderPopUp.SIMPageOrderPopUp(self.driver).assert_in_region_and_sim_amount(
                region_should_be=region,
                amount_of_sim_cards_should_be=amount_of_sim_cards
            )
            SIMPageOrderPopUp.SIMPageOrderPopUp(self.driver).order_sim_popup_for_delivery()

    def activate_sim_steps(self, workplace_name, save_activation_or_cancel_activation):
        self.wait_for_element(self.activate_sim_btn).click()
        self.wait_for_element(self.activate_sim_chose_wp_dropdown).click()
        self.wait_for_element(self.activate_sim_chose_in_list + str(workplace_name) + "')]").click()
        self.wait_for_element(self.generate_code_btn).click()
        if save_activation_or_cancel_activation is 'save_activation':
            code = self.wait_for_element(self.code).text
            self.wait_for_element(self.popup_activation_ok_btn).click()
            return code
        elif save_activation_or_cancel_activation is 'cancel_activation':
            self.wait_for_element(self.popup_activation_cancel_btn).click()
            return
        else:
            return AttributeError

    def cancel_sim_activation(self, sim_wp_name_to_cancel_activation_of):
        self.click_sim_in_list(sim_name_to_click=sim_wp_name_to_cancel_activation_of)
        self.wait_for_element(self.popup_activation_cancel_btn).click()
        pass
