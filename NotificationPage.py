# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class NotificationPage(init_driver.InitDriver):

    url_path = "/settings/notifications"
    title = "Уведомления"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Уведомления')]"
    checkbox_on_sms = ".//*[@id='NotificationsForm_deliveryBySms-styler']"
    checkbox_on_email = ".//*[@id='NotificationsForm_deliveryByEmail-styler']"
    threshold_field = ".//*[@id='NotificationsForm_threshold']"
    save_btn = ".//*[@id='threshold-form']//input[@type='submit']"
    email_for_notification = ".//*[@id='NotificationsForm_email']"
    phone_for_notification = ".//*[@id='NotificationsForm_phone']"

    def go_to_notification_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_notification_page(self):
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
        pass

    def check_checkbox_on_sms(self):
        self.wait_for_element(self.checkbox_on_sms).click()
        pass

    def check_checkbox_on_email(self):
        self.wait_for_element(self.checkbox_on_email).click()
        pass

    def set_threshold(self, threshold):
        self.wait_for_element(self.threshold_field).clear()
        self.wait_for_element(self.threshold_field).send_keys(threshold)
        pass

    def save_notifications(self):
        self.wait_for_element(self.save_btn).click()
        pass

    def get_email_for_notification(self):
        email_for_notification = self.wait_for_element(self.email_for_notification).text
        return email_for_notification

    def get_phone_for_notification(self):
        phone_for_notification = self.wait_for_element(self.phone_for_notification).text
        return phone_for_notification
