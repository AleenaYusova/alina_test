# -*- coding: utf-8 -*-
#
import inspect

import time

import CLI
import Helper
import init_driver


class WorkplaceSettings(init_driver.InitDriver):

    get_title = ".//*[@id='modal-users-edit']//*[@class='popup__title']"
    title = "Настройка рабочего места"
    name = ".//*[@id='WorkPlace_name']"
    position = ".//*[@id='WorkPlace_position']"
    cli = ".//*[@id='WorkPlace_cli-styler']"
    email_field = ".//*[@id='Cabinet_email']"
    internal_number_field = ".//*[@id='Cabinet_internalNumber']"
    password_field = ".//*[@id='Cabinet_password']"
    limit_filed = ".//*[@id='Cabinet_monthLimit']"
    fax_btn = ".//*[@id='Cabinet_faxAccess-styler']"
    save_btn = "//*[@id='modal-users-edit']//input[@value='Сохранить']"
    delete_workplace_btn = ".//*[@id='modal-users-edit']//a[@class='link-dashed delete-workplace']"
    sign_agreement_btn = "//button/span[contains(.,'Подписать')]"
    sign_agreement_ok_btn = "//button[@type='button']"
    cancel_sign_agreement_btn = "//button/span[contains(.,'Отмена')]"
    set_password_equipment_checkbox = ".//*[@id='Cabinet_usePasswordFromEquipment-styler']"
    sip_id_btn = "//*[@id='SipAccount_type-styler']/parent::*/*[contains(.,'SIP ID')]"
    voip_number = ".//*[@id='SipAccount_voip_number']"
    generate_password = "//*[@id='modal-users-edit']//a[contains(.,'Сгенерировать пароль')]"
    shown_password = ".//*[@id='SipAccount_password_shownPassword']"
    ip_static_btn = "//*[@id='SipAccount_type-styler']/parent::*/*[contains(.,'IP-адрес')]"
    insert_ip = ".//*[@id='IpAccount_voip_number']"
    ip_type_dropdown = ".//*[@id='IpAccount_protocol-styler']"
    ip_type_udp = "//li[contains(.,'UDP')]"
    ip_type_tcp = "//li[contains(.,'TCP')]"
    create_lk_btn = ".//*[@id='modal-users-edit']//a[contains(.,'Создать')]"
    close_popup = ".//*[@id='modal-users-edit']//span[@class='popup__close']"
    ip_static_error_msg = ".//*[@id='modal-users-edit']//span[contains(.,'IP-адрес')]/parent::*" \
                          "/parent::*//div[@class='popup__error']"
    sign_btn = "//button/span[contains(.,'Подписать')]"

    def make_sure_its_workplace_settings_page(self):
        print(inspect.stack()[0][3])
        assert self.title in self.wait_for_element(self.get_title).text

    def get_workplace_name(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.name).text

    def set_workplace_position(self, workplace_position):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.position).clear()
        self.wait_for_element(self.position).send_keys(workplace_position)

    def get_workplace_position(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.position).text

    def set_cli(self, number):
        print(inspect.stack()[0][3])
        CLI.CLI(self.driver).set_cli(cli_locator=self.cli, number=number)
        pass

    def get_cli(self):
        print(inspect.stack()[0][3])
        return CLI.CLI(self.driver).get_cli_clean_number(cli_locator=self.cli)

    def set_email(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.email_field).clear()
        self.wait_for_element(self.email_field).send_keys(email)

    def get_email(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.email_field).text

    def set_internal_number(self, internal_number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.internal_number_field).clear()
        self.wait_for_element(self.internal_number_field).send_keys(internal_number)

    def set_password(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.set_password_equipment_checkbox).click()

    def set_limit(self, limit):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.limit_filed).clear()
        self.wait_for_element(self.limit_filed).send_keys(limit)

    def get_limit(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.limit_filed).text

    def click_fax_checkbox(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.fax_btn).click()

    def save_workplace_form(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.save_btn).click()
        try:
            time.sleep(5)
            self.wait_for_element(self.sign_agreement_btn).click()
            return
        except UserWarning:
            time.sleep(5)
            return

    def delete_workplace(self, sign_agreement=True):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.delete_workplace_btn).click()
        if sign_agreement is True:
            self.wait_for_element(self.sign_agreement_btn).click()
            self.wait_for_element(self.sign_agreement_ok_btn).click()
            time.sleep(10)
        elif sign_agreement is False:
            self.wait_for_element(self.cancel_sign_agreement_btn).click()
        else:
            return AttributeError

    def set_workplace_name(self, workplace_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.name).send_keys(str(workplace_name))
        pass

    def set_sip_id(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.sip_id_btn).click()
        pass

    def get_sip_number(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.voip_number).text
        pass

    def set_sip_password(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.generate_password).click()
        pass

    def get_sip_password(self):
        print(inspect.stack()[0][3])
        return self.wait_for_element(self.shown_password).text
        pass

    def create_workplace_with_ip_static(self, udp_or_tcp, workplace_name, workplace_position=None, create_lk=False):
        print(inspect.stack()[0][3])

        def set_correct_ip_static():
            print(inspect.stack()[0][3])
            while True:
                try:
                    self.wait_for_element(self.insert_ip).send_keys(Helper.generate_ip_static())
                    self.wait_for_element(self.save_btn).click()
                    time.sleep(5)
                    self.driver.find_element_by_xpath(self.ip_static_error_msg)
                    print(True)
                    return True
                except UserWarning:
                    print(False)
                    return False

        self.wait_for_element(self.ip_static_btn).click()
        set_correct_ip_static()
        self.wait_for_element(self.ip_type_dropdown).click()

        if udp_or_tcp is 'udp':
            self.wait_for_element(self.ip_type_udp).click()
        elif udp_or_tcp is 'tcp':
            self.wait_for_element(self.ip_type_tcp).click()
        else:
            return AttributeError
        self.wait_for_element(self.name).send_keys(workplace_name)
        self.wait_for_element(self.position).send_keys(workplace_position)

        if create_lk is False:
            self.wait_for_element(self.save_btn).click()
            self.wait_for_element(self.sign_btn).click()
            time.sleep(30)
        elif create_lk is True:
            self.wait_for_element(self.create_lk_btn).click()
        else:
            return AttributeError

    def create_lk(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.create_lk_btn).click()
        pass

    def cancel_workplace_creation(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.close_popup).click()
        pass
