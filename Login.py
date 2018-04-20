# -*- coding: utf-8 -*-
#

import inspect
# import unittest
# import sys
import time
import init_driver


class Login(init_driver.InitDriver):

    emailField = "//*[@id='CustomerLoginForm_email']"
    passwordField = "//*[@id='CustomerLoginForm_password']"
    loginButton = ".//*[@id='login-form']//input[@value='Войти']"
    errorMessageEmailLocator = "//div[@class='popup__error' and contains(.,'Необходимо заполнить поле «Email».')]"
    errorMessagePasswordLocator = "//div[@class='popup__error' and contains(.,'Неверный email или пароль')]"
    showPasswordLocator = ".//*[@id='showPassword-styler']"
    passwordRecoveryButton = "//form[@id='login-form']//span[text() = 'Восстановить пароль?']"
    passwordRecoveryEmailField = ".//*[@id='CustomerPasswordRecovery_email']"
    passwordRecoverySendButton = "//form[@id='passwordRecovery-form']//input[@value='Отправить']"
    passwordRecoveryClosePopup = "//form[@id='passwordRecovery-form']//span[@class='popup__close']"

    def go_to_login(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def insert_email(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.emailField).send_keys(email)

    def insert_password(self, password):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordField).send_keys(password)

    def click_log_in_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.loginButton).click()
        time.sleep(3)

    def error_msg_email(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.errorMessageEmailLocator)

    def error_msg_password(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.errorMessagePasswordLocator)

    def show_password(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.showPasswordLocator).click()

    def password_recovery(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordRecoveryButton).click()

    def password_recovery_insert_email(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordRecoveryEmailField).send_keys(email)

    def send_password_recovery(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordRecoverySendButton).click()

    def close_popup_password_recovery(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.passwordRecoveryClosePopup).click()

# if __name__ == '__main__':
#     unittest.main(argv=[sys.argv[0]])
