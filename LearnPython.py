# # -*- coding: utf-8 -*-
# #
import datetime
import random
from urllib.parse import urlparse

import time
#
# import datetime
#
# today = datetime.date.today()
# print today
# print today.isoweekday()


#
# def url_work():
#     o = 'https://business.mtt.ru/user/login'
#     o = urlparse(o)
#     print(o.path)
#     pass
# url_work()

# def func(a):
#     c = a.strftime('%d.%m.%Y')
#     return c
#
# b = datetime.date.today()
# print(func(b))

# azazaz = 'azaz'
# print(len(azazaz))
# b = 2.5646
# c = 0.3

# new = int(azaza)
# print(new)
# new = int(b)
# print(new)
# new = int(c)
# print(new)
#
# print(listy[1])
#
# did_box_btn = "azazaz"
#
# def get_list_of_locators(service_name):
#     """ Method returns_list_of_locators_depending_on_the_service_name """
#     if service_name is 'did':
#         xpath = ''.join((service_name, "_box_btn"))
#         return (xpath)
#
#
# print(get_list_of_locators('did'))

# def funct():
#     "comment text comment text comment text comment text"
#     var="123"
#     if var==str("condition"):
#         print "var='condition'"
#     elif var==str("somethingelse"):
#         print "var='somethingelse'"
#         print "123"
#     else:
#         print AttributeError
#
# funct()
# print (funct().__doc__)
#
#
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# timestamp = int(time.time())
# timestamp = str(timestamp)
# print("7" + str(timestamp).replace(timestamp[0:1], '9'))
# print(timestamp[0:])
# .replace(str(timestamp)[0:1], '8'))


# timestamp = int(time.time())
# timestamp = str(timestamp) # .replace(str(timestamp)[0:1], '8')
# print(timestamp)
#

# print(".".join(map(str, (random.randint(0, 255) for _ in range(4)))))



# def get_short_number(number):
#     number = number.replace('-', '')
#     number = number.replace('(', '')
#     number = number.replace(')', '')
#     number = number.replace(' ', '')
#     number = number.replace('+', '')
#     number = number.replace('8800', '7800')
#     number = number.replace('8804', '7804')
#     return number
#
#
# phone = "+7 (499) 709-01-11 "
#
# # short = get_short_number(phone)
#
#
# def full(param):
#     param = get_short_number(param)
#     print(param)
#     param = param.replace(param[1:4], ' (' + param[1:4] + ') ')
#     param = param.replace(param[8:11], param[8:11] + '-')
#     param = param.replace(param[12:14], param[12:14] + '-')
#     return param
#
# print(full(phone))


# from PortalMonBaseTestClass import *
# from MttHelper import *
# import random
#
# class AuthClientTest(PortalMonBaseTestClass):
#
#     drv = None
#     select_auth = '/user/login'
#     select_callProcessing = '/settings/callProcessing'
#     #URL сайта
#     URL_MTT_PORTAL = None
#
#     #login & password
#     staticLogin = None
#     staticPassword = None
#
#     @classmethod
#     def setUpClass(cls):
#         cls.drv = PortalMonBaseTestClass.get_driver(sys.argv[1])
#
#     def test001_login(self):
#         drv = self.drv
#         drv.get("http://testrail:8080/index.php?/runs/overview/17")
#         self.wait_for_element_tobe_clickable(".//*[@id='name']").send_keys("ssergeev@mtt.ru")
#         self.wait_for_element_tobe_clickable(".//*[@id='password']").send_keys("$eh-$eR-6j0gkk")
#         self.wait_for_element_tobe_clickable(".//*[@id='content']/form/div[4]/button").click()
#
#     def test002_loop(self):
#         drv = self.drv
#         count = 0
#         while True:
#             try:
#                 drv.get("http://testrail:8080/index.php?/runs/overview/17")
#                 self.wait_for_element_tobe_clickable("//div[@id='active']/div/div[3]//div[@class='summary-title text-ppp']/a").click()
#                 self.wait_for_element_tobe_clickable("//*[@id='content-header']/div/span[1]").click()
#                 self.wait_for_element_tobe_clickable(".//*[@id='confirmDialog']/div[3]/a[1]").click()
#                 count=count+1
#             except:
#                 print "count is"
#                 print count
#                 break
#
#
#
#
# if __name__ == '__main__':
#     unittest.main(argv=[sys.argv[0]])

# def myfunction(c):
#     a = 0
#     b = 0
#     if c is 0:
#         a = a >= 14
#         b = b >= 14
#     elif c > 0:
#         a = a
#
# phone = "795551112233"
# print(phone[1:7:])

# def test(phrase,letter):
#     counter = 0
#
#     for i in phrase:
#         if i == letter:
#             counter = counter + 1
#
#     print(counter)
# test(phrase="vkxvhkjv",letter='v')

def get_timestamp():
    timestamp = int(time.time())
    return str(timestamp)

# @staticmethod
# def generate_series_passport():
#     timestamp = int(time.time())
#     return str(timestamp[0:4:1])
