# -*- coding: utf-8 -*-
#
import inspect
import init_driver


class WorkplaceCallForwardSchema(init_driver.InitDriver):

    internal_number = "//*[@id='workplaces-refresh-redirect-scheme']//span[@class='fmc_text-big']"
    xpath_beginning = "//*[@id='workplaces-refresh-redirect-scheme']"
    serial_callforward = "//div[@data-level='0']"
    parallel_callforward = "//div[@data-level][last()]"
    add_fmc_icon = "//div[@class='fmc-icon fmc_add-icon']"
    add_firstpartofxpath = "//*[@id='workplaces-refresh-redirect-scheme']//div[@data-type='"
    delete_firstpartofxpath = "//*[@id='workplaces-refresh-redirect-scheme']//span[contains(.,'"
    delete_secondpartofxpath = "')]/parent::*/parent::*//span[@class='fmc-icon fmc_drop-icon']"
    timeout_xpath_dropdown = "//*[@id='workplaces-refresh-redirect-scheme']//div[@class='jq-selectbox__text']"
    element_in_timeout_dropdown_list = "//*[@id='workplaces-refresh-redirect-scheme']" \
                                       "//div[@class='jq-selectbox__dropdown']//li[contains(.,'"
    save_fmc_schema = ".//*[@id='workplaces-refresh-redirect-scheme']//input[@class='button-red fmc_tree-save']"

    def get_internal_number(self):
        print(inspect.stack()[0][3])
        internal_number = self.wait_for_element(self.internal_number).text
        return internal_number
        pass

    def add_fmc_element_into_schema(self, serial_or_parallel_callforward, name_of_fmc_element):
        """ Функция по добавлению переадресации в схему """
        print(inspect.stack()[0][3])

        """ Используя вспомогатеьную функцию if_function в классе CallforwardLevelsHelper
        формируем xpath в зависимости от переданного 
        в данную функцию параметра serial_or_parallel_callforward"""
        callforward_level_xpath = CallforwardLevelsHelper.if_function(serial_or_parallel_callforward)

        """ Делается клик по значку добавления """
        self.wait_for_element(callforward_level_xpath + self.add_fmc_icon).click()

        """ Делается клик по иконке, в зависимости от имени переданного 
        в данную функцию переметром name_of_fmc_element """
        self.wait_for_element(callforward_level_xpath + self.add_firstpartofxpath +
                              str(name_of_fmc_element) + "']").click()

    def delete_fmc_element_from_schema(self, name_of_fmc_element):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.delete_firstpartofxpath +
                              str(name_of_fmc_element) + self.delete_secondpartofxpath).click()

    def set_timouts_between_serial_callforwardings(self, timeout_time_to_set):
        print(inspect.stack()[0][3])
        timeout_to_intert_in_xpath = int(timeout_time_to_set)
        self.driver.find_elements_by_xpath(self.timeout_xpath_dropdown).click()
        self.driver.find_elements_by_xpath(self.element_in_timeout_dropdown_list +
                                           str(timeout_to_intert_in_xpath) + "')]")

    def save_call_forward_schema(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.save_fmc_schema).click()
        pass


class CallforwardLevelsHelper:
    @staticmethod
    def if_function(serial_or_parallel_callforward):
        if serial_or_parallel_callforward is 'serial':
            xpath_to_return = WorkplaceCallForwardSchema.xpath_beginning + \
                              WorkplaceCallForwardSchema.serial_callforward
            return str(xpath_to_return)
        elif serial_or_parallel_callforward is 'parallel':
            xpath_to_return = WorkplaceCallForwardSchema.xpath_beginning + \
                              WorkplaceCallForwardSchema.parallel_callforward
            return str(xpath_to_return)
        else:
            print(AttributeError)
            return AttributeError
