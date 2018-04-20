# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
from selenium.webdriver.common.keys import Keys
import init_driver
import CLI


class WorkplacePage(init_driver.InitDriver):

    url_path = "/settings/workPlaces"
    title = "Рабочие места"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Рабочие места')]"
    cli_btn = ".//*[@id='vpbx-workplaces']//*[@href='/settings/workPlaces/getDefaultCliForm']"
    cli_locator = ".//*[@id='DefaultCliForm_defaultCli-styler']"
    save_cli_btn = ".//*[@id='modal-setting-filter']//input[@type='submit' and @value='Сохранить']"
    close_cli_popup = ".//*[@id='modal-setting-filter']//*[@class='popup__close']"
    search_workplace_field = ".//*[@id='WorkPlacesFilter_search']"
    first_workplace_in_list = ".//*[@id='item-list-container']/div[2]"
    lks_btn = "/div[last()]/*"
    vpbx_change = ".//*[@id='vpbx-workplaces']//a[@class='link-dashed change-params']"
    download_excel_btn = ".//*[@id='generate_workplace_list']//a[contains(.,'Экспорт в Excel')]"
    create_new_workplace_btn = ".//*[@id='vpbx-workplaces']//a[@class='button-red floatL workplace-create']"
    no_workplace_in_list = ".//*[@id='item-list-container']//div[@class='layout__cell empty']"

    def go_to_workplace_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    """ Не реализовано https://jira.mtt.ru:8443/browse/MTTBPORTAL-5706"""
    # def make_sure_its_action_history_page(self):
    #     print(inspect.stack()[0][3])
    #
    #     """ проверка правильности пути в url """
    #     def make_sure_its_correct_url():
    #         print(inspect.stack()[0][3])
    #         assert self.driver.current_url in (SetUpFile.SetUpFile.url_path + self.url_path)
    #         pass
    #
    #     """ сравнение title страницы """
    #     def make_sure_its_correct_title():
    #         self.wait_for_element(self.navigationBarElement).click()
    #         time.sleep(3)
    #         assert self.driver.title in self.title
    #         pass
    #
    #     """ вызов описанных функций """
    #     make_sure_its_correct_url()
    #     make_sure_its_correct_title()
    #     pass

    def search_workplace(self, workplace_name_to_search):
        self.wait_for_element(self.search_workplace_field).clear()
        self.wait_for_element(self.search_workplace_field).send_keys(workplace_name_to_search)
        self.wait_for_element(self.search_workplace_field).send_keys(Keys.ENTER)

    def click_create_new_workplace_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.create_new_workplace_btn).click()

    def set_cli(self, number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.cli_btn).click()
        CLI.CLI(self.driver).set_cli(cli_locator=self.cli_locator, number=number)
        self.wait_for_element(self.save_cli_btn).click()

    def get_cli(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.cli_btn).click()
        number_to_return = CLI.CLI(self.driver).get_cli_clean_number(cli_locator=self.cli_locator)
        self.wait_for_element(self.save_cli_btn).click()
        return number_to_return

    def go_to_workplace_settings(self, workplace_name_to_open):
        print(inspect.stack()[0][3])
        self.search_workplace(workplace_name_to_search=workplace_name_to_open)
        self.wait_for_element(self.first_workplace_in_list).click()

    def go_lks(self, workplace_to_go_into_lks):
        print(inspect.stack()[0][3])
        self.search_workplace(workplace_name_to_search=workplace_to_go_into_lks)
        self.wait_for_element(self.first_workplace_in_list + self.lks_btn).click()

    def open_vpbx_settings_popup(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.vpbx_change).click()

    def download_excel_file(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.download_excel_btn).click()

    def make_sure_there_is_no_such_workplace(self, workplace_name):
        self.search_workplace(workplace_name_to_search=workplace_name)
        self.wait_for_element(self.no_workplace_in_list)
