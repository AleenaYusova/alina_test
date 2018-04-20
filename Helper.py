import datetime
import inspect
import random
import time
import init_driver
from selenium.webdriver.common.action_chains import ActionChains


class GetShortNumber:
    """ Возвращает номер в формате '74997090111' """
    @staticmethod
    def get_short_number(number):
        number = number.replace('-', '')
        number = number.replace('(', '')
        number = number.replace(')', '')
        number = number.replace(' ', '')
        number = number.replace('+', '')
        number = number.replace('8800', '7800')
        number = number.replace('8804', '7804')
        return number


class GetFullNumber:
    """ Возвращает номер в формате '7 (499) 709-01-11' """
    @staticmethod
    def get_full_number(number):
        number = GetShortNumber.get_short_number(number)
        number = number.replace(number[1:4],   ' (' + number[1:4] + ') ')
        number = number.replace(number[8:11],  number[8:11] + '-')
        number = number.replace(number[12:14], number[12:14] + '-')
        return number


class DateAndTime:
    @staticmethod
    def convert_date_into_ddmmyyyy(date_to_convert):
        converted_date = date_to_convert.strftime('%d.%m.%Y')
        return converted_date

    @staticmethod
    def get_current_date():
        current_date = datetime.date.today()
        DateAndTime.convert_date_into_ddmmyyyy(current_date)
        return current_date

    @staticmethod
    def print_current_date_and_time():
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class GenerateCustomerData:

    @staticmethod
    def generate_customer_login_email():
        timestamp = int(time.time())
        return str(timestamp) + "@auto.test"

    @staticmethod
    def generate_customer_phone_number():
        timestamp = int(time.time())
        timestamp = str(timestamp)
        return "7" + str(timestamp).replace(timestamp[0:1], '9')

class ActionChainsClass(init_driver.InitDriver):
    def move_to_element_and_click(self, element_to_move_to, element_to_click):
        try:
            print(inspect.stack()[0][3])
            actions = ActionChains(self.driver)
            element_to_move_to = self.driver.find_element_by_xpath(element_to_move_to)
            actions.move_to_element(element_to_move_to)
            time.sleep(0.1)
            element_to_click = self.driver.find_element_by_xpath(element_to_click)
            actions.click(element_to_click)
            print("actions.perform()")
            actions.perform()
        except:
            print("ActionChainsClass EXCEPT")


def generate_ip_static():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))


def get_timestamp():
    timestamp = int(time.time())
    return str(timestamp)


class ScreenShot(init_driver.InitDriver):
    def take_screen_shot_in_base64_format(self):
        print(self.driver.get_screenshot_as_base64())
