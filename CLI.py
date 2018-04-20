# -*- coding: utf-8 -*-
#
import unittest
import sys
import Helper
import init_driver


class CLI(init_driver.InitDriver):

    def set_cli(self, cli_locator, number):
        self.wait_for_element(cli_locator).click()
        full_path_to_the_number_to_set = cli_locator+"//ul/li[contains(.,'"+number+"')]"
        self.wait_for_element(full_path_to_the_number_to_set).click()
        pass

    def get_cli_origin_number(self, cli_locator):
        originumbertype = self.wait_for_element(cli_locator).text
        return originumbertype
        pass

    def get_cli_clean_number(self, cli_locator):
        short_number_type = self.wait_for_element(cli_locator).text
        short_number_type = Helper.GetShortNumber.get_short_number(short_number_type)
        return short_number_type
        pass

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[0]])
