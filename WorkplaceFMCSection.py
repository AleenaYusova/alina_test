# -*- coding: utf-8 -*-
#
import init_driver


class WorkplaceFMCSection(init_driver.InitDriver):

    sip = ".//*[@id='SipAccount_voip_number-styler']/div/div[1][text()]"
    show_password = ".//*[@id='showPassword-styler']"
    password = ".//*[@id='SipAccount_password_shownPassword']"
    generate_password = ".//*[@id='wp-sip']//a[contains(.,'Сгенерировать пароль')]"
    tab = ".//*[@id='workPlaceSettings-form-tabs']//ul[@class='tabs-titles horizontal']/li[@data-content='wp-']"
    activation_btn = ".//*[@id='wp-sim']//input[@class='button-red action-activate']"
    generate_code_btn = ".//*[@id='modal-select-options']//button[contains(.,'Сгенерировать код')]"
    code = ".//*[@id='modal-select-options']//div[@class='code sim-generated-code_value']"
    activation_ok_btn = ".//*[@id='modal-select-options']//button[contains(.,'Ок')]"
    cancel_activation_btn = ".//*[@id='modal-select-options']//button[contains(.,'Отмена активации')]"
    info_on_activation_sim = ".//*[@id='wp-sim']//input[@value='Информация об активации']"
    click_softphone = ".//*[@id='SoftphoneAccount_isEnabled-styler']"
    softphone_email = ".//*[@id='SoftphoneAccount_email']"
    itunes = ".//*[@id='wp-softphone']/div/div[3]/div[2]/a[1]"
    googleplay = ".//*[@id='wp-softphone']/div/div[3]/div[2]/a[2]"
    skype_name = ".//*[@id='AdminWorkPlace_skype']"
    skype_radio_btn = ".//*[@id='AdminWorkPlace_isSkypeEnabled-styler']"
    save_btn = ".//*[@id='modal-users-edit']//input[@type='submit'][@value='Сохранить']"

    def get_sip_login(self):
        return self.wait_for_element(self.sip).text
        pass

    def get_sip_password(self):
        self.wait_for_element(self.show_password).click()
        return self.wait_for_element(self.password).text
        pass

    def set_sip_password(self):
        self.wait_for_element(self.generate_password).click()
        pass

    def go_to_tab(self, tab_name):
        """
        :param tab_name: 'sim', 'sip', 'softphone', 'skype'
        """
        self.wait_for_element(self.tab + str(tab_name) + "']").click()
        pass

    def sim_tab_activate_sim(self):
        self.wait_for_element(self.activation_btn).click()
        pass

    def generate_fmc_check_code(self):
        self.wait_for_element(self.generate_code_btn).click()
        pass

    def finish_activation(self):
        self.wait_for_element(self.activation_ok_btn).click()
        pass

    def get_activation_info(self):
        self.wait_for_element(self.info_on_activation_sim).click()
        pass

    def cancel_sim_activation(self):
        self.wait_for_element(self.cancel_activation_btn).click()
        pass

    def return_check_code(self):
        return self.wait_for_element(self.code).text
        pass

    def click_softphone_radio_btn(self):
        self.wait_for_element(self.click_softphone).click()

    def get_softphone_email(self):
        return self.wait_for_element(self.softphone_email).text

    def check_itunes_link(self):
        self.wait_for_element(self.itunes).click()
        current_url = self.driver.current_url
        assert current_url.netloc in 'itunes.apple.com'
        self.driver.close()

    def check_googleplay_link(self):
        self.wait_for_element(self.googleplay).click()
        current_url = self.driver.current_url
        assert current_url.netloc in 'play.google.com'
        self.driver.close()

    def connect_skype(self):
        self.wait_for_element(self.skype_radio_btn).click()

    def insert_skype_name(self, skype_name):
        self.wait_for_element(self.skype_name).clear()
        self.wait_for_element(self.skype_name).send_keys(skype_name)

    def save_workplace_popup(self):
        self.wait_for_element(self.save_btn).click()
