# -*- coding: utf-8 -*-
#
import inspect
import unittest
from urllib.parse import urlparse
import time
import sys
import Header
import SetUpFile
import init_driver


class HomePage(init_driver.InitDriver):

    title = "Рабочий стол"
    homePageTitle = "//h1[contains(.,'Рабочий стол')]"
    homePageFooter = "//div[@class='footer__list']"
    homePageMGP = "//div[@class='layout__half']//td[contains(.,'МГП')]/parent::tr/td[2]"
    homePageReceivables = "//div[@class='layout__half']//td[contains(.,'Дебиторская задолженность')]/parent::tr/td[2]"
    homePageNextChargeOff = "//div[@class='layout__half']//td[contains(.,'Следующее списание')]/parent::tr/td[2]"
    homePageStatus = "//div[@class='layout__half']//td[contains(.,'Ваш статус')]/parent::tr/td[2]"
    homePageCreditLimit = "//div[@class='layout__half']//td[contains(.,'Кредитный лимит')]/parent::tr/td[2]"
    homePageMinimalCharge = "//div[@class='layout__half']//td[contains(.,'Минимальная сумма для оплаты')]" \
                            "/parent::tr/td[2]"
    homePageVoiceMailData = "//span[contains(.,'Голосовая почта')]/parent::h2/parent::div//" \
                            "div[@class='layout__sub-half']"
    homePageVoiceMailLink = "//span[contains(.,'Голосовая почта')]/parent::h2/parent::div//" \
                            "a[@href and contains(.,'Вся голосовая почта')]"
    homePageFaxLink = "//span[contains(.,'Факсы')]/parent::h2/parent::div//a[@href and contains(.,'Все факсы')]"
    homePageLSnumber = "//div[@class='lR']//div[@class='lR__info-nmbr']/b"
    homePageBalance = "//div[@class='lR']//div[contains(.,'Баланс')]/b"
    homePageAbonPlata = "//div[@class='lR']//div[contains(.,'Аб. пл')]/b"
    homePageMakeChargeBtn = "//div[@class='lR']//div/a[@href='/accounting/payments']"
    homePageManagerName = "//div[@class='lR']//div/*[@class='lR__question-manager']"
    homePageSupportBtn = "//div[@class='lR']//a[@class='button-red manager-help']"
    homePageSupportFIO = ".//*[@id='HelpForm_username']"
    homePageSupportPhone = ".//*[@id='HelpForm_phone']"
    homePageSupportEmail = ".//*[@id='HelpForm_email']"
    homePageSupportComment = ".//*[@id='HelpForm_message']"
    homePageSupportSubmitBtn = ".//*[@id='help-submit']"
    homePageCurrentDiskSpace = "//div[@class='diagram diagram_space']//span[@class='diagram__total-numb']"
    homePageDiskSpaceCost = "//div[@class='diagram diagram_space']//div[contains(.,'Стоимость')]/b"
    homePageLinkDID = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/did']"
    homePageLinkFREE = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/free']"
    homePageLinkDEF = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/def']"
    homePageLinkVoIP = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/voip']"
    homePageLinkVPBX = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/vpbx']"
    homePageLinkVR = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/vr']"
    homePageLinkSIM = "//ul[@class='slide__list slide__list_desctop']/li/a[@href='/services/smm']"
    homePageLinkChangeLK = "//div[@title='Изменение количества личных кабинетов']//a[contains(.,'Изменить')]"
    homePageLKcount = "//div[@title='Изменение количества личных кабинетов']//span[@class='diagram__total-numb']"
    homePageLKcost = "//div[@title='Изменение количества личных кабинетов']//div[contains(.,'Стоимость:')]/b"
    sign_contract_btn = "//div[@class='news__title news__title_black'][contains(.,'У вас не подписан договор')]" \
                        "/parent::*//a[contains(.,'Подписать договор')]"

    def go_to_home_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc
        self.driver.get(new_url)
        pass

    def make_sure_its_home_page(self):
        print(inspect.stack()[0][3])

        """ проверка правильности пути в url """
        def make_sure_its_correct_url():
            print(inspect.stack()[0][3])
            Header.Header(self.driver).click_home_btn()
            assert self.driver.current_url in SetUpFile.SetUpFile.url_path + "/"

        """ сравнение title страницы """
        def make_sure_its_correct_title():
            print(inspect.stack()[0][3])
            # self.wait_for_element(Header.Header(self.driver).click_home_btn())
            print(self.title.encode('utf-8'))
            time.sleep(3)
            print(self.driver.title.encode('utf-8'))
            assert self.title in self.driver.title

        """ вызов описанных функций """
        make_sure_its_correct_url()
        make_sure_its_correct_title()
        pass

    def get_mgp(self):
        print(inspect.stack()[0][3])
        mgp = self.wait_for_element(self.homePageMGP).text
        mgp = mgp.replace(" ", "")
        mgp = mgp.replace("руб.", "")
        return mgp
        pass

    def get_receivables(self):
        receivables = self.wait_for_element(self.homePageReceivables).text
        receivables = receivables.replace(" ", "")
        receivables = receivables.replace("руб.", "")
        return receivables
        pass

    def get_next_charge_off_date(self):
        print(inspect.stack()[0][3])
        next_charge_off_date = self.wait_for_element(self.homePageNextChargeOff).text
        next_charge_off_date = next_charge_off_date.replace(" ", "")
        next_charge_off_date = next_charge_off_date[0:10]
        return next_charge_off_date
        pass

    def get_next_charge_off_sum(self):
        print(inspect.stack()[0][3])
        next_charge_off_sum = self.wait_for_element(self.homePageNextChargeOff).text
        next_charge_off_sum = next_charge_off_sum.replace(" ", "")
        next_charge_off_sum = next_charge_off_sum.replace("руб.", "")
        next_charge_off_sum = next_charge_off_sum[11:]
        return next_charge_off_sum

    def get_current_status(self):
        print(inspect.stack()[0][3])
        status = self.wait_for_element(self.homePageStatus).text
        if status in "Активен":
            return "Active"
        elif status in "Тестовый":
            return "Test"
        elif status in "Неактивен":
            return "NotActive"
        elif status in "Заблокирован":
            return "Blocked"
        else:
            return "ERROR in homePage.getCurrentStatus"
        pass

    def get_credit_limit(self):
        print(inspect.stack()[0][3])
        creditlimit = self.wait_for_element(self.homePageCreditLimit).text
        creditlimit = creditlimit.replace(" ", "")
        creditlimit = creditlimit.replace("руб.", "")
        return creditlimit
        pass

    def get_minimal_charge(self):
        print(inspect.stack()[0][3])
        minimalcharge = self.wait_for_element(self.homePageMinimalCharge).text
        minimalcharge = minimalcharge.replace(" ", "")
        minimalcharge = minimalcharge.replace("руб.", "")
        return minimalcharge
        pass

    def get_voice_mail_data(self):
        print(inspect.stack()[0][3])
        voice_mail_data = self.wait_for_element(self.homePageVoiceMailData)
        voice_mail_data = voice_mail_data.split('+')
        del voice_mail_data[0]
        return voice_mail_data
        pass

    def go_voice_mail(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageVoiceMailLink).click()
        pass

    def get_fax_data(self):
        print(inspect.stack()[0][3])
        """ Не реализовано """
        print("getFaxData method is not developed \n")
        pass

    def go_fax(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageFaxLink).click()
        pass

    def get_ls_number(self):
        print(inspect.stack()[0][3])
        lsnumber = self.wait_for_element(self.homePageLSnumber).text
        lsnumber = lsnumber.encode('utf-8')
        lsnumber = str(lsnumber).replace('№ ', '')
        return lsnumber
        pass

    def get_balance(self):
        print(inspect.stack()[0][3])
        balance = self.wait_for_element(self.homePageBalance).text
        balance = balance.replace(' ', '')
        return balance
        pass

    def get_abon_plata(self):
        print(inspect.stack()[0][3])
        abonplata = self.wait_for_element(self.homePageAbonPlata).text
        abonplata = abonplata.replace(' ', '')
        return abonplata
        pass

    def go_make_charge(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageMakeChargeBtn).click()
        pass

    def get_manager_name(self):
        print(inspect.stack()[0][3])
        managername = self.wait_for_element(self.homePageManagerName).text
        return managername
        pass

    def go_manager_support(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportBtn).click()
        pass

    def set_fio_in_support_form(self, fio):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportFIO).clear()
        self.wait_for_element(self.homePageSupportFIO).send_keys(fio)
        pass

    def set_phone_in_support_form(self, phone):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportPhone).clear()
        self.wait_for_element(self.homePageSupportPhone).send_keys(phone)
        pass

    def set_email_in_support_form(self, email):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportEmail).clear()
        self.wait_for_element(self.homePageSupportEmail).send_keys(email)
        pass

    def set_comment_in_support_form(self, comment_text):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportComment).clear()
        self.wait_for_element(self.homePageSupportComment).send_keys(comment_text)
        pass

    def submit_in_support_form(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageSupportSubmitBtn).click()
        pass

    def get_current_disk_space(self):
        print(inspect.stack()[0][3])
        current_disk_space = self.wait_for_element(self.homePageCurrentDiskSpace).text
        return current_disk_space
        pass

    def get_disk_space_cost(self):
        print(inspect.stack()[0][3])
        disk_space_cost = self.wait_for_element(self.homePageDiskSpaceCost).text
        disk_space_cost = disk_space_cost.replace(' ', '')
        return disk_space_cost
        pass

    def set_lk(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkChangeLK).click()
        pass

    def get_lk_count(self):
        print(inspect.stack()[0][3])
        lkcount = self.wait_for_element(self.homePageLKcount).text
        return lkcount
        pass

    def get_lk_cost(self):
        print(inspect.stack()[0][3])
        lkcost = self.wait_for_element(self.homePageLKcost).text
        return lkcost
        pass

    def go_did_number_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkDID).click()
        pass

    def go_free_number_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkFREE).click()
        pass

    def go_mobile_number_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkDEF).click()
        pass

    def go_voip_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkVoIP).click()
        pass

    def go_vpbx_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkVPBX).click()
        pass

    def go_voice_records_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkVR).click()
        pass

    def go_sim_page_by_clicking_box(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.homePageLinkSIM).click()

    def click_sign_contract_btn(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.sign_contract_btn).click()


if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
