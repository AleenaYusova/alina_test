# -*- coding: utf-8 -*-
#
import init_driver


class VPBXSettings(init_driver.InitDriver):

    pop_up_vpbx_settings = ".//*[@id='modal-select-options']"
    insert_vpbx_count_field = ".//*[@id='VpbxProductConfigurator_workPlaceCount']"
    number_of_vpbx_from_string = ".//*[@id='modal-select-options']//div[contains(.,'личных кабинетов')]/b"
    vpbx_price = ".//*[@id='workplaceCount-cost']"
    save_vpbx_btn = ".//*[@id='modal-select-options']//input[@type='submit']"

    def make_sure_its_vpbx_settings_page(self):
        self.wait_for_element(self.pop_up_vpbx_settings)
        pass

    def set_vpbx_number(self, vpbx_count):
        self.wait_for_element(self.insert_vpbx_count_field).clear()
        self.wait_for_element(self.insert_vpbx_count_field).send_keys(vpbx_count)
        pass

    def get_number_of_vpbx(self):
        number_from_vpbx_count_field = self.wait_for_element(self.insert_vpbx_count_field).text
        number_of_vpbx_from_string = self.wait_for_element(self.number_of_vpbx_from_string).text
        assert number_of_vpbx_from_string in number_from_vpbx_count_field
        return number_of_vpbx_from_string
        pass

    def get_vpbx_price(self):
        vpbx_price = self.wait_for_element(self.vpbx_price).text
        vpbx_price = vpbx_price.replace(' руб.', '')
        return vpbx_price
        pass

    def save_vpbx_settings(self):
        self.wait_for_element(self.save_vpbx_btn).click()
        pass
