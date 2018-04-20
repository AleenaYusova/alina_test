# -*- coding: utf-8 -*-
#
import inspect
import time
import init_driver

class MTTB_Page(init_driver.InitDriver):

    mttb_save_btn = "//a[@class='button-red contract-edit-submit'][contains(.,'Сохранить')]"
    mttb_services_btn = "//a[@class='menu__a nav'][contains(.,'Услуги')]"
    mttb_web_widgets_btn = "//a[@class='lR__it  nav'][contains(.,'Web-виджеты')]"
    mttb_to_plug_ww_btn = "//a[@class='button-red'][contains(.,'Подключить')]"

    def go_to_mttb_page(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def click_mttb_save_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_save_btn).click()
        time.sleep(3)

    def click_mttb_services_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_services_btn).click()
        time.sleep(3)

    def click_mttb_web_widgets_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_web_widgets_btn).click()
        time.sleep(4)

    def click_mttb_to_plug_ww_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mttb_to_plug_ww_btn).click()
        time.sleep(4)











