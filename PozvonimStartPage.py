# -*- coding: utf-8 -*-
#
import inspect
import time
import init_driver


class PozvonimStartPage(init_driver.InitDriver):

    loginButtonEnter = "//li[@class='loginButton hs-menu-item hs-menu-depth-1'][contains(.,'Войти')]"
    loginButtonRegistration = "//li[@class='registerButton hs-menu-item hs-menu-depth-1'][contains(.,'Зарегистрироваться')]"

    def go_to_pzv_start_page(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def click_log_in_btn_enter(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.loginButtonEnter).click()
        time.sleep(3)

    def click_log_in_btn_registration(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.loginButtonRegistration).click()
        time.sleep(3)