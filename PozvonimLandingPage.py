# -*- coding: utf-8 -*-
#
import inspect
import time
import init_driver
import pyperclip

class PozvonimLandingPage(init_driver.InitDriver):

    landing_site = "//div[@class='navbar-header']"
    save_changes = "//button[@class='btn btn-primary'][contains(.,'Save changes')]"
    callback_btn =  "//div[@class='callback__arrow-icon']"
    chat_btn = "//div[@id='pozvonim-wrapper-chat']"
    pzvIFrameChat = 'pozvonim-chat-frame'
    pzvIFrameCallback = 'callback-frame'
    helloworldField = '//*[@id="pozvonim-widget-chat"]'
    enter_btn = "//a[@class='form__send-message form__send-message--visible']"
    clientphone_field = "//input[@class='field__inner field__input js__field-phone input phone']"
    waiting_for_call_btn = "//button[@id='pozvonim-button-element'][contains(.,'Жду звонка')]"

    def go_to_pzv_landing_page(self, url_to_go):
        print(inspect.stack()[0][3])
        self.driver.get(url_to_go)

    def click_landing_site(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.landing_site).click()
        time.sleep(3)
        print(pyperclip.paste())
        time.sleep(3)

    def click_save_changes(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.save_changes).click()
        time.sleep(3)

    def refresh_page1(self):
        self.driver.refresh()
        time.sleep(4)

    def click_chat_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.chat_btn).click()
        time.sleep(3)

    def insert_helloworld(self, helloworld):
        print(inspect.stack()[0][3])
        self.driver.switch_to_frame(self.pzvIFrameChat)
        self.wait_for_element(self.helloworldField).send_keys(helloworld)
        self.driver.switch_to_default_content()
        time.sleep(3)

    def click_enter_btn(self):
        print(inspect.stack()[0][3])
        self.driver.switch_to_frame(self.pzvIFrameChat)
        self.wait_for_element(self.enter_btn).click()
        self.driver.switch_to_default_content()
        time.sleep(3)

    def click_callback_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.callback_btn).click()
        time.sleep(3)

    def insert_clientphone(self, clientphone):
        print(inspect.stack()[0][3])
        self.driver.switch_to_frame(self.pzvIFrameCallback)
        self.wait_for_element(self.clientphone_field).send_keys(clientphone)
        self.driver.switch_to_default_content()
        time.sleep(3)

    def click_waiting_for_call_btn(self):
        print(inspect.stack()[0][3])
        self.driver.switch_to_frame(self.pzvIFrameCallback)
        self.wait_for_element(self.waiting_for_call_btn).click()
        self.driver.switch_to_default_content()
        time.sleep(20)
