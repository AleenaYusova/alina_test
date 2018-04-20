# -*- coding: utf-8 -*-
#
import time
import Helper
import init_driver


class JournalFilters(init_driver.InitDriver):

    show_results_btn = ".//*[@id='filter-form']//input[@type='submit']"
    filter_type_dropdown = ".//*[@id='JournalFilter_type-styler']"
    filter_by_employee = ".//*[@id='JournalFilter_type-styler']//li[contains(.,'Сотрудник')]"
    filter_by_employee_dropdown = ".//*[@id='s2id_JournalFilter_employee']/*"
    filter_by_employee_dropdown_input = ".//*[@id='select2-drop']/div/input"
    filter_by_employee_dropdown_first_in_list = ".//*[@id='select2-drop']/ul/li[1]"
    filter_by_group = ".//*[@id='JournalFilter_type-styler']//li[contains(.,'Группа')]"
    filter_by_group_dropdown = ".//*[@id='s2id_JournalFilter_group_id']/*"
    filter_by_group_dropdown_input = ".//*[@id='select2-drop']/div/input"
    filter_by_group_dropdown_first_in_list = ".//*[@id='select2-drop']/ul/li[1]"
    filter_by_number = ".//*[@id='JournalFilter_type-styler']//li[contains(.,'Номер')]"
    filter_by_number_input = ".//*[@id='JournalFilter_number']"
    filter_by_period = ".//*[@id='JournalFilter_type-styler']//li[contains(.,'Период')]"
    filter_by_period_date_from = ".//*[@id='JournalFilter_date_from']"
    filter_by_period_date_to = ".//*[@id='JournalFilter_date_to']"

    def set_filter_by_employee(self, employee_name_to_filter):
        self.wait_for_element(self.filter_type_dropdown).click()
        self.wait_for_element(self.filter_by_employee).click()
        self.wait_for_element(self.filter_by_employee_dropdown).click()
        self.wait_for_element(self.filter_by_employee_dropdown_input).send_keys(employee_name_to_filter)
        time.sleep(1)
        self.wait_for_element(self.filter_by_employee_dropdown_first_in_list).click()
        self.wait_for_element(self.show_results_btn).click()
        pass

    def set_filter_by_group(self, group_name_to_filter):
        self.wait_for_element(self.filter_type_dropdown).click()
        self.wait_for_element(self.filter_by_group).click()
        self.wait_for_element(self.filter_by_group_dropdown).click()
        self.wait_for_element(self.filter_by_group_dropdown_input).send_keys(group_name_to_filter)
        time.sleep(1)
        self.wait_for_element(self.filter_by_group_dropdown_first_in_list).click()
        self.wait_for_element(self.show_results_btn).click()
        pass

    def set_filter_by__number(self, number_to_filter):
        self.wait_for_element(self.filter_type_dropdown).click()
        self.wait_for_element(self.filter_by_number).click()
        number_to_filter = Helper.GetShortNumber.get_short_number(number_to_filter)
        self.wait_for_element(self.filter_by_number_input).send_keys(number_to_filter)
        self.wait_for_element(self.show_results_btn).click()
        pass

    def set_filter_by_period(self, date_from, date_to):
        self.wait_for_element(self.filter_type_dropdown).click()
        self.wait_for_element(self.filter_by_period).click()
        self.wait_for_element(self.filter_by_period_date_from).send_keys(date_from)
        self.wait_for_element(self.filter_by_period_date_to).send_keys(date_to)
        self.wait_for_element(self.show_results_btn).click()
        pass
