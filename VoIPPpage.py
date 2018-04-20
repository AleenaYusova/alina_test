# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class VoIPPpage(init_driver.InitDriver):

    url_path = "/services/voip"
    title = "Исходящая связь VoIP"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Исходящая связь VoIP')]"
    first_part_of_xpath = ".//*[@id='outgoingVoip-form']//div[@data-attribute='name'][contains(.,'"
    price_part_of_xpath = "')]/parent::div//div[@data-attribute='price']/*"
    checkbox_part_of_xpath = "')]/parent::div//*[@type='checkbox']"
    save_btn = "//input[@type='submit' and @value='Сохранить']"

    def go_to_voip_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_voip_page(self):
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

    def get_price_of_direction(self, name_of_direction_to_get_price_of):
        price = self.wait_for_element(self.first_part_of_xpath + str(name_of_direction_to_get_price_of)
                                      + self.price_part_of_xpath).text
        return price
        pass

    def check_direction(self, name_of_direction_to_check):
        self.wait_for_element(self.first_part_of_xpath + str(name_of_direction_to_check) +
                              self.checkbox_part_of_xpath).click()
        pass

    def save_voip(self):
        self.wait_for_element(self.save_btn).click()
        pass
