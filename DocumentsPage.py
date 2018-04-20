# -*- coding: utf-8 -*-
#
import inspect
from urllib.parse import urlparse
import time
import SetUpFile
import init_driver


class DocumentsPage(init_driver.InitDriver):

    url_path = "/accounting/documents"
    title = "Документы"
    navigationBarElement = "//div[@class='lR__dark']/*[contains(.,'Документы')]"
    namesOfDocumentsInTheListToDownload = "//div[@class='clearfix basket__line see_doc']/div[@documentid]"
    namesOfDocumentsInTheListFirstPartOfXpath = "//div[@class='clearfix basket__line see_doc']["
    namesOfDocumentsInTheListSecondPartOfXpath = "]/div[@documentid]"
    dateOfDocumentsInTheList = "//div[@class='clearfix basket__line see_doc']/div[2]"
    changeDocumentBtn = "//table[@class='tbl-grey']//a[text()='Изменить договор']"
    downloadApplicationBtn = "//table[@class='tbl-grey']//a[text()='Скачать заявления']"
    invoiceField = ".//*[@id='Invoice_sum']"
    getInvoiceBtn = ".//*[@id='Invoice_sum']/parent::div/button[@class='button-red get-payment']"

    def go_to_documents_page(self):
        print(inspect.stack()[0][3])
        old_url = urlparse(self.driver.current_url)
        new_url = old_url.scheme + '://' + old_url.netloc + self.url_path
        self.driver.get(new_url)
        pass

    def make_sure_its_documents_page(self):
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

    def download_document(self, name_of_document_to_download=None):
        print(inspect.stack()[0][3])
        if name_of_document_to_download is None:
            self.wait_for_element(self.namesOfDocumentsInTheListToDownload).click()
        elif name_of_document_to_download is not None:
            self.wait_for_element(self.namesOfDocumentsInTheListToDownload + "[contains(.,'"
                                  + str(name_of_document_to_download) + "')]").click()
        else:
            print(AttributeError)
            return AttributeError
        pass

    def get_document_date(self, document_name=None):
        print(inspect.stack()[0][3])
        if document_name is None:
            date = self.wait_for_element(self.dateOfDocumentsInTheList).text
            return date
        elif document_name is not None:
            date = self.wait_for_element(self.dateOfDocumentsInTheList + "[contains(.,'" +
                                         str(document_name) + "')]").text
            return date
        else:
            print(AttributeError)
            return AttributeError
        pass

    def get_document_name(self, document_position_in_list=1):
        print(inspect.stack()[0][3])
        name = self.wait_for_element(self.namesOfDocumentsInTheListFirstPartOfXpath + str(document_position_in_list)
                                     + self.namesOfDocumentsInTheListSecondPartOfXpath).text
        return name
        pass

    def change_document(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.changeDocumentBtn).click()
        pass

    def download_invoice(self, sum_of_invoice=100):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.invoiceField).clear()
        self.wait_for_element(self.invoiceField).send_keys(str(sum_of_invoice))
        self.wait_for_element(self.getInvoiceBtn).click()
