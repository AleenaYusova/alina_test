# -*- coding: utf-8 -*-
#
import datetime
import inspect
import unittest
import sys
import init_driver
import time


class CallbackPage(init_driver.InitDriver):

    text_of_page_title = "Настройка Callback"
    callback_page_title = "//form[@id='callback-settings-form']//*[@class='popup__title']"
    mainTab = "//*[@id='callback-settings-form']//div[@class='tabs-block']//a[text()='Основные']"
    catchleaveTab = "//*[@id='callback-settings-form']//div[@class='tabs-block']//a[text()='Отлавливать уход']"
    scheduleTab = "//*[@id='callback-settings-form']//div[@class='tabs-block']//a[text()='Расписание']"
    textTab = "//*[@id='callback-settings-form']//div[@class='tabs-block']//a[text()='Текст']"
    appearanceTab = "//*[@id='callback-settings-form']//div[@class='tabs-block']//a[text()='Внешность']"
    websiteAdressField = ".//*[@id='CallbackNumber_name']"
    geoTargetingChecked = "//*[@id='CallbackNumber_geoTargeting-styler']" \
                          "[@class='jq-checkbox jq-checkbox popup__checkbox checked']"
    geoTargetingNotChecked = "//*[@id='CallbackNumber_geoTargeting-styler']" \
                             "[@class='jq-checkbox jq-checkbox popup__checkbox']"
    openingDelayChecked = ".//*[@id='CallbackNumber_expandWithADelay-styler']" \
                          "[@class='jq-checkbox jq-checkbox popup__checkbox checked']"
    openingDelayNotChecked = ".//*[@id='CallbackNumber_expandWithADelay-styler']" \
                             "[@class='jq-checkbox jq-checkbox popup__checkbox']"
    openingDelayMinutesSelector = ".//*[@id='CallbackNumber_delayMinutes-styler']"
    openingDelaySetMinutes = ".//*[@id='CallbackNumber_delayMinutes-styler']//ul/li[text()='"
    openingDelaySecondsSelector = ".//*[@id='CallbackNumber_delaySeconds-styler']"
    openingDelaySetSeconds = ".//*[@id='CallbackNumber_delaySeconds-styler']//ul/li[text()='"
    whoGetsCallFirst = ".//*[@id='select-toCallTheFirst-styler']"
    managerGetsCallFirst = ".//*[@id='select-toCallTheFirst-styler']//ul/li[text()='Менеджер']"
    clientGetsCallFirst = ".//*[@id='select-toCallTheFirst-styler']//ul/li[text()='Клиент']"
    howOftenWidgetAppearsElement = ".//*[@id='select-frequency-styler']"
    widgetAppearsEverytime = ".//*[@id='select-frequency-styler']//ul/li[text()='При каждом посещении']"
    widgetAppearsOncePerDay = ".//*[@id='select-frequency-styler']//ul/li[text()='Ежедневно']"
    widgetAppearsOncePerWeek = ".//*[@id='select-frequency-styler']//ul/li[text()='Еженедельно']"
    CLIelement = ".//*[@id='select-cli-styler']"
    notificationCheckBoxChecked = ".//*[@id='CallbackNumber_sendOnInit-styler']" \
                                  "[@class='jq-checkbox jq-checkbox popup__checkbox checked']"
    notificationCheckBoxNotChecked = ".//*[@id='CallbackNumber_sendOnInit-styler']" \
                                     "[@class='jq-checkbox jq-checkbox popup__checkbox']"
    jscode = ".//*[@id='CallbackNumber_code']"
    catchleaveCheckboxChecked = ".//*[@id='leaving_catch-change-styler']" \
                                "[@class='jq-checkbox jq-checkbox popup__checkbox checked']"
    catchleaveCheckboxNotChecked = ".//*[@id='leaving_catch-change-styler']" \
                                   "[@class='jq-checkbox jq-checkbox popup__checkbox']"
    timezoneElement = ".//*[@id='select-timetable_timezone-styler']"
    selectTimezoneElement = ".//*[@id='select-timetable_timezone-styler']//ul/li[contains(.,'"
    dayOfWeekCheckboxFirstPartOfXpath = ".//*[@id='cb-timetable']/div[@class='clearfix']" \
                                        "/div[@class!='clearfix cb-fg-row cb_days-line']["
    dayOfWeekCheckboxCheckedSecondPartOfXpath = "]//span[@class='jq-checkbox jq-checkbox popup__checkbox " \
                                                "cb_schedule-day_enable checked']"
    dayOfWeekCheckboxNotCheckedSecondPartOfXpath = "]//span[@class='jq-checkbox " \
                                                   "jq-checkbox popup__checkbox cb_schedule-day_enable']"
    mainBtnTextElement = ".//*[@id='CallbackNumber_buttonText']"
    mainMsgTextElement = ".//*[@id='CallbackNumber_text']"
    whilecallBtnTextElement = ".//*[@id='CallbackNumber_cancelText']"
    whilecallMsgTextElement = ".//*[@id='CallbackNumber_calledText']"
    errorBtnTextElement = ".//*[@id='CallbackNumber_errorButtonText']"
    errorMsgTextElement = ".//*[@id='CallbackNumber_errorText']"
    saveBtn = ".//*[@id='callback-settings-form']//*[@class='button-red button-red_float_right submit-settings' " \
              "AND @value='Сохранить']"
    closePopUpBtn = ".//*[@id='callback-settings-form']//*[@class='popup__close']"

    def make_sure_its_callback_page(self):
        print(inspect.stack()[0][3])
        callback_page_title = self.wait_for_element(self.callback_page_title).text
        assert self.text_of_page_title in callback_page_title
        pass

    def go_to_main_tab(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.mainTab).click()
        pass

    def set_website_address(self, website_adress):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.websiteAdressField).clear()
        self.wait_for_element(self.websiteAdressField).send_keys(website_adress)
        pass

    def geo_targeting(self, need_to_be_checked=True):
        print(inspect.stack()[0][3])

        # если чекбокс должен быть отмечен, то needToBeChecked==True
        if need_to_be_checked is True:
            # в try мы делаем проверку. Если чекбокс соответствует ожиданию, то return True
            try:
                self.wait_for_element(self.geoTargetingChecked)
                return True
            # Если чекбокс не соответствует ожиданию, то мы делаем клик по чекбоксу
            # убеждаемся, что теперь его состояние соотвествует и возвращаем return True
            except UserWarning:
                self.wait_for_element(self.geoTargetingNotChecked).click()
                self.wait_for_element(self.geoTargetingChecked)
                return True

        # если чекбокс не должен быть отмечен, то needToBeChecked==False
        elif need_to_be_checked is False:
            # в try мы делаем проверку. Если чекбокс соответствует ожиданию, то return True
            try:
                self.wait_for_element(self.geoTargetingNotChecked)
                return True
            # Если чекбокс не соответствует ожиданию, то мы делаем клик по чекбоксу
            # убеждаемся, что теперь его состояние соотвествует и возвращаем return True
            except UserWarning:
                self.wait_for_element(self.geoTargetingChecked).click()
                self.wait_for_element(self.geoTargetingNotChecked)
                return True
        else:
            return AttributeError
        pass

    def opening_delay(self, need_to_be_checked=True, number_of_minutes_for_opening_delay=0,
                      number_of_seconds_for_opening_delay=0):
        print(inspect.stack()[0][3])

        # метод по установке минут
        def set_minutes():
            self.wait_for_element(self.openingDelayMinutesSelector).click()
            self.wait_for_element(self.openingDelaySetMinutes + str(number_of_minutes_for_opening_delay) + "']").click()
            pass

        # метод по установке секунд
        def set_seconds():
            self.wait_for_element(self.openingDelayMinutesSelector).click()
            self.wait_for_element(self.openingDelaySetMinutes + str(number_of_seconds_for_opening_delay) + "']").click()
            pass

        # если в функцию openingDelay передан параметр needToBeChecked=True
        # (то есть "Разворачивать с задержкой" должно быть включено)
        if need_to_be_checked is True:
            while False:
                # проверяем соответствует ли условие, если да,
                # то вызываем функции по установке минут и секунд и выходим из try
                try:
                    self.wait_for_element(self.openingDelayChecked)
                    set_minutes()
                    set_seconds()
                    return True
                # если условие не выполнено,
                # в except делаем клик по элименту, и выолняем блок try снова
                except UserWarning:
                    self.wait_for_element(self.openingDelayNotChecked).click()

        # если в функцию openingDelay передан параметр needToBeChecked=False
        # (то есть "Разворачивать с задержкой" должно быть выключено)
        elif need_to_be_checked is False:
            while False:
                # проверяем соответствует ли условие, если да, то выходим
                try:
                    self.wait_for_element(self.openingDelayNotChecked)
                    return True
                # если условие не выполнено,
                # то делаем клик по элименту, и снова идем в блок try для проверки
                except UserWarning:
                    self.wait_for_element(self.openingDelayChecked).click()
        else:
            return AttributeError
        pass

    def set_who_gets_call_first(self, manager=True):
        print(inspect.stack()[0][3])
        if manager is True:
            self.wait_for_element(self.whoGetsCallFirst).click()
            self.wait_for_element(self.managerGetsCallFirst).click()
        elif manager is False:
            self.wait_for_element(self.whoGetsCallFirst).click()
            self.wait_for_element(self.clientGetsCallFirst).click()
        else:
            return AttributeError
        pass

    def how_often_widget_appears(self, options="everytime"):
        print(inspect.stack()[0][3])
        # В качестве аргумента функции можно передать
        # один из трех параметров: "everytime", "oncePerDay", "oncePerWeek"
        if options == str("everytime"):
            self.wait_for_element(self.howOftenWidgetAppearsElement).click()
            self.wait_for_element(self.widgetAppearsEverytime).click()
        elif options == str("oncePerDay"):
            self.wait_for_element(self.howOftenWidgetAppearsElement).click()
            self.wait_for_element(self.widgetAppearsEverytime).click()
        elif options == str("oncePerWeek"):
            self.wait_for_element(self.howOftenWidgetAppearsElement).click()
            self.wait_for_element(self.widgetAppearsEverytime).click()
        else:
            print(AttributeError)
        pass

    def set_cli(self, number):
        # print(inspect.stack()[0][3])
        # return self.CLIelement
        pass

    def call_back_order_notification(self, notification_checked=True):
        print(inspect.stack()[0][3])
        # если чек бокс notification должен быть Checked
        if notification_checked is True:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(self.notificationCheckBoxChecked)
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except UserWarning:
                self.wait_for_element(self.notificationCheckBoxNotChecked).click()
                self.wait_for_element(self.notificationCheckBoxChecked)

        # если чек бокс notification должен быть Not Checked
        elif notification_checked is False:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(self.notificationCheckBoxNotChecked)
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except UserWarning:
                self.wait_for_element(self.notificationCheckBoxChecked).click()
                self.wait_for_element(self.notificationCheckBoxNotChecked)
        else:
            print(AttributeError)
        pass

    def get_js_code(self):
        print(inspect.stack()[0][3])
        js_code = self.wait_for_element(self.jscode).text
        return js_code
        pass

    def go_catch_leave_tab(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.catchleaveTab).click()
        pass

    def catch_leave_check(self, catch_leave_checked=True):
        print(inspect.stack()[0][3])
        # если чек бокс должен быть Checked
        if catch_leave_checked is True:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(self.catchleaveCheckboxChecked)
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except Warning:
                self.wait_for_element(self.catchleaveCheckboxNotChecked).click()
                self.wait_for_element(self.catchleaveCheckboxChecked)

        # если чек бокс должен быть Not Checked
        elif catch_leave_checked is False:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(self.catchleaveCheckboxNotChecked)
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except Warning:
                self.wait_for_element(self.catchleaveCheckboxChecked).click()
                self.wait_for_element(self.catchleaveCheckboxNotChecked)
        else:
            print(AttributeError)
        pass

    def go_schedule_tab(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.scheduleTab).click()
        pass

    def select_timezone(self, timezone):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.timezoneElement).click()
        self.wait_for_element(self.selectTimezoneElement + timezone + "')]").click()
        pass

    def set_schedule(self, day_of_week_checked=True, what_day=datetime.date.today()):
        print(inspect.stack()[0][3])
        whatday = what_day.isoweekday()

        # xpath для отмеченного чек бокса
        xpath_for_checked_checkbox = self.dayOfWeekCheckboxFirstPartOfXpath + str(whatday) \
                                    + self.dayOfWeekCheckboxCheckedSecondPartOfXpath
        # xpath для не отмеченного чек бокса
        xpath_for_not_checked_checkbox = self.dayOfWeekCheckboxFirstPartOfXpath + str(whatday)\
                                        + self.dayOfWeekCheckboxNotCheckedSecondPartOfXpath

        # если чек бокс должен быть Checked
        if day_of_week_checked is True:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(xpath_for_checked_checkbox)
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except UserWarning:
                self.wait_for_element(xpath_for_not_checked_checkbox).click()
                self.wait_for_element(xpath_for_checked_checkbox)

        # если чек бокс должен быть Not Checked
        elif day_of_week_checked is False:
            # проверяем соотвествуте ли условию
            try:
                self.wait_for_element(xpath_for_not_checked_checkbox)
                return
            # если условию не соотвествует -- делаем клик по чекбоксу
            # и убеждаемся, что чекбокс отмечен
            except UserWarning:
                self.wait_for_element(xpath_for_checked_checkbox).click()
                self.wait_for_element(xpath_for_not_checked_checkbox)
        else:
            print(AttributeError)
            return AttributeError
        pass

    def go_text_tab(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.textTab).click()
        pass

    def set_text(self, main_btn_text, main_msg_text, while_call_btn_text, while_call_msg_text,
                 error_btn_text, error_msg_text):
        print(inspect.stack()[0][3])

        def clear_and_send_keys(xpath, text):
            self.wait_for_element(xpath).clear()
            self.wait_for_element(xpath).send_keys(text)

        clear_and_send_keys(self.mainBtnTextElement, main_btn_text)
        clear_and_send_keys(self.mainMsgTextElement, main_msg_text)
        clear_and_send_keys(self.whilecallBtnTextElement, while_call_btn_text)
        clear_and_send_keys(self.whilecallMsgTextElement, while_call_msg_text)
        clear_and_send_keys(self.errorBtnTextElement, error_btn_text)
        clear_and_send_keys(self.errorMsgTextElement, error_msg_text)
        pass

    def go_appearance_tab(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.appearanceTab).click()
        pass

    def save_callback(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.saveBtn).click()
        time.sleep(10)

    def close_callback_settings_window(self):
        print(inspect.stack()[0][3])
        self.wait_for_element(self.closePopUpBtn).click()

#
# if __name__ == '__main__':
#     unittest.main(argv=[sys.argv[0]])
