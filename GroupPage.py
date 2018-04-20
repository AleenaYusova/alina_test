# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
from selenium.webdriver.common.keys import Keys
import SetUpFile
import init_driver


class GroupPage(init_driver.InitDriver):

    url_path = "/settings/groups"
    title = "Группы"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Группы')]"
    addGroupBtn = ".//*[@id='vpbx-groups']//a[@class='button-red action-add-group']"
    groupName = ".//*[@id='Group_name']"
    internalNumber = ".//*[@id='Group_internalNumber']"
    groupEmail = ".//*[@id='Group_email']"
    sequenceSelector = ".//*[@id='select-order-styler']"
    sequenceList = ".//*[@id='settings-form']//option[@value='"
    soundSelector = ".//*[@id='select-melodies-styler']"
    soundListIthem = ".//*[@id='select-melodies-styler']//li[contains(.,'Carlos Saura, Always Ahead')]"
    saveBtn = "//input[@type='submit']"
    save_add_workplace_btn = ".//*[@id='members-form']//input[@type='submit']"
    searchField = ".//*[@id='GroupsFilter_search']"
    groupInList = ".//*[@id='vpbx-groups']//div[@groupid]"
    addWorkplaceToGroupBtn = ".//*[@id='vpbx-group-members']//a[@class='button-red add-members']"
    workplaceToSelectInListToAddToGroupFirstPartOfXpath = ".//*[@id='members-list-container']//" \
                                                          "div[@class='layout__cell members-name'][contains(.,'"
    workplaceToSelectInListToAddToGroupSecondPartOfXpath = "')]/parent::div//" \
                                                           "*[@class='jq-checkbox smpl-checkbox add-member']"
    saveWorkplaceAddingBtn = ".//*[@id='members-form']//input[@type='submit' AND @value='Сохранить']"
    deleteWorkplaceFromGroupBtnFirstPartOfXpath = "//div[@id='sortable-members']//b[contains(.,'"
    deleteWorkplaceFromGroupBtnSecondPartOfXpath = "')]/parent::div/parent::div//" \
                                                   "a[@class='layout__basket-bg-bl delete-member']"
    confirmDeleteWorkplaceFromGroupBtn = "//div[@aria-describedby='confirm-dialog']//button[contains(.,'Да')]"
    settingsBtn = ".//*[@id='vpbx-groups']/div[2]/div[3]/div[4]/div"
    deleteGroupBtn = ".//*[@id='settings-form']//a[contains(.,'Удалить группу')]"
    internal_number = ".//*[@id='vpbx-groups']/div[2]/div[3]/div[1]"
    conferm_delete_group_btn = "//button/*[contains(.,'Удалить')]"
    conferm_delete_ok_group_btn = "//*[@class='ui-dialog-buttonset']//button[@type='button']/span[contains(.,'OK')]"

    def go_to_group_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_group_page(self):
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

    def click_add_group(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.addGroupBtn).click()

    def set_group_name(self, group_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.groupName).clear()
        self.wait_for_element(self.groupName).send_keys(group_name)

    def set_group_internal_number(self, group_internal_number):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.internalNumber).clear()
        self.wait_for_element(self.internalNumber).send_keys(group_internal_number)

    def get_group_internal_number(self, group_name_to_get_internal_number_of):
        print(inspect.stack()[0][3])
        self.search_group(group_name=group_name_to_get_internal_number_of)
        group_internal_number = self.wait_for_element(self.internal_number).text
        return group_internal_number

    def set_group_email(self, group_email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.groupEmail).clear()
        self.wait_for_element(self.groupEmail).send_keys(group_email)

    def set_sequence(self, sequence_is_random_or_simultaneous_or_order):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.sequenceSelector).click()
        self.wait_for_element(self.sequenceList + str(sequence_is_random_or_simultaneous_or_order) + "']").click()

    def set_group_sound(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.soundSelector).click()
        self.wait_for_element(self.soundListIthem).click()

    def click_save_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.saveBtn).click()
        time.sleep(10)

    def search_group(self, group_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.searchField).clear()
        self.wait_for_element(self.searchField).send_keys(group_name)
        self.wait_for_element(self.searchField).send_keys(Keys.ENTER)

    def add_workplace_to_group(self, workplace_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.groupInList).click()
        self.wait_for_element(self.addWorkplaceToGroupBtn).click()
        self.wait_for_element(self.workplaceToSelectInListToAddToGroupFirstPartOfXpath + str(workplace_name) +
                              self.workplaceToSelectInListToAddToGroupSecondPartOfXpath).click()
        time.sleep(3)
        self.wait_for_element(self.save_add_workplace_btn).click()
        time.sleep(10)

    def delete_workplace_from_group(self, workplace_name):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.groupInList).click()
        self.wait_for_element(self.deleteWorkplaceFromGroupBtnFirstPartOfXpath + str(workplace_name)
                              + self.deleteWorkplaceFromGroupBtnSecondPartOfXpath).click()
        self.wait_for_element(self.confirmDeleteWorkplaceFromGroupBtn).click()

    def go_group_settings(self, group_name):
        print(inspect.stack()[0][3])
        self.search_group(group_name)
        self.wait_for_element(self.settingsBtn).click()

    def delete_group(self, group_name):
        print(inspect.stack()[0][3])
        self.go_group_settings(group_name)
        self.wait_for_element(self.deleteGroupBtn).click()
        self.wait_for_element(self.conferm_delete_group_btn).click()
        time.sleep(10)
        self.wait_for_element(self.conferm_delete_ok_group_btn).click()
        time.sleep(5)
