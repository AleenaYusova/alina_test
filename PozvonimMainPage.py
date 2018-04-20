# -*- coding: utf-8 -*-
#
import inspect
import time
import init_driver


class PozvonimMainPage(init_driver.InitDriver):

    profile_btn =  "//li[@data-controller='Profile'][contains(.,'Профиль')]"

    def go_to_pzv_start_page(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def click_profile_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.profile_btn).click()
        time.sleep(3)




