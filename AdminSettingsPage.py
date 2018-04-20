# -*- coding: utf-8 -*-
#
import inspect
import unittest
import sys
import init_driver


class AdminSettingsPage(init_driver.InitDriver):

    title = "Администратор"
    adminSettingsPageTitle = "//*[@id='modal-users-edit']/div[3]/div[1]/div[3]/strong"
    adminSettingsPageNameFieldLocator = "//*[@id='AdminWorkPlace_name']"
    cliSelectorLocator = "//*[@id='AdminWorkPlace_cli-styler']"
    adminPositionLocator = "//*[@id='AdminWorkPlace_position']"
    adminEmailLocator = "//*[@id='AdminCabinet_email']"
    showAdminPasswordLocator = ".//*[@id='showLkPassword-styler']"
    adminPasswordLocator = ".//*[@id='AdminCabinet_password_shownPassword']"
    adminPasswordRepeatLocator = ".//*[@id='AdminCabinet_passwordRepeat_shownPassword']"
    adminPhoneNumberLocator = "//*[@id='AdminCabinet_phone']"
    internalNumberLocator = "//*[@id='AdminCabinet_internalNumber']"
    adminLimitLocator = "//*[@id='AdminCabinet_monthLimit']"
    adminGroupsNoData = "//*[@for='AdminCabinet_groups']/parent::div/div[contains(.,'Нет данных')]"
    adminGroupsNamesList = "//div[@class and contains(.,'Группы')]/label[contains(.,'Группы')]" \
                           "/parent::div//ul[@class='select2-choices']"

    def make_sure_its_admin_settings_page(self):
        print(inspect.stack()[0][3])
        admin_name_value = self.wait_for_element(self.adminSettingsPageTitle).text
        assert self.title in admin_name_value
        pass

    def cli_setcli(self, number):
        print(inspect.stack()[0][3])
        # CLI.setCLI(self.cliSelectorLocator, number)
        pass

    def get_cli_origin_number_type(self, clilocator):
        print(inspect.stack()[0][3])
        # CLI.getCLIOriginNumberType(self.cliSelectorLocator)
        pass

    def get_cli_clean_number_type(self, clilocator):
        print(inspect.stack()[0][3])
        # CLI.getCLICleanNumberType(self.cliSelectorLocator)
        pass

    def set_admin_position(self, position):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.adminPositionLocator).clear()
        self.wait_for_element(self.adminPositionLocator).send_keys(position)
        pass

    def get_admin_workplace_email(self):
        print(inspect.stack()[0][3])
        admin_email = self.wait_for_element(self.adminEmailLocator).text
        return admin_email
        pass

    def set_admin_workplace_email(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.adminEmailLocator).clear()
        self.wait_for_element(self.adminEmailLocator).send_keys(email)
        pass

    def get_admin_workplace_password(self):
        print(inspect.stack()[0][3])
        password_admin = self.wait_for_element(self.adminPasswordLocator).text
        return password_admin
        pass

    def set_admin_workplace_password(self, password):
        print(inspect.stack()[0][3])
        self.show_admin_password()
        self.wait_for_element(self.adminPasswordLocator).send_keys(password)
        self.wait_for_element(self.adminPasswordRepeatLocator).send_keys(password)
        pass

    def show_admin_password(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.showAdminPasswordLocator).click()
        pass

    def get_admin_mobile_number(self):
        print(inspect.stack()[0][3])
        phone = self.wait_for_element(self.adminPhoneNumberLocator).text
        return phone
        pass

    def set_admin_mobile_number(self, number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.adminPhoneNumberLocator).clear()
        self.wait_for_element(self.adminPhoneNumberLocator).send_keys(number)
        pass

    def get_admin_internal_number(self):
        print(inspect.stack()[0][3])
        number = self.wait_for_element(self.internalNumberLocator).text
        return number
        pass

    def set_admin_internal_number(self, number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.internalNumberLocator).clear()
        self.wait_for_element(self.internalNumberLocator).send_keys(number)
        pass

    def get_admin_limit(self):
        print(inspect.stack()[0][3])
        limit = self.wait_for_element(self.adminLimitLocator).text
        return limit
        pass

    def set_admin_limit(self, limit):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.adminLimitLocator).clear()
        self.wait_for_element(self.adminLimitLocator).send_keys(limit)
        pass

    def get_admin_group_name_list(self):
        print(inspect.stack()[0][3])
        """ Если в поле Группы 'Нет данных' -- то метод возвращает 'None'. """
        try:
            self.wait_for_element(self.adminGroupsNoData)
            return None
        finally:
            """ Если в поле Группы есть имена групп -- все имена записываются в перменную,
            затем этот метод возвращает имена в виде массива.
            ИМЕНА ГРУПП НЕ ДОЛЖНЫ СОДЕРЖАТЬ ПРОБЕЛОВ"""
            group_names = self.wait_for_element(self.adminGroupsNamesList).text
            list_of_names = group_names.split('\n')
            return list_of_names
        pass

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
