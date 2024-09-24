import time

import pytest
from selenium.webdriver.common.by import (By)
from base_pages.Login_Admin_page import Login_Admin_page
from utilities.read_properties import Read_config
from utilities.Custom_Logging import Log_Maker
from utilities import excel_utils


class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()

    logger = Log_Maker.log_gen()
    path = '/home/manikrishna/Pycharm/Python_Automation/testdata/Open_cartLoginDetails.xlsx'
    status_list = []
    @pytest.mark.sanity
    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info(
            "*********_/home/manikrishna/Pycharm/Python_Automation/testdata/Open_cartLoginDetails.xlsx************")
        self.logger.info("*********Verificatin of admin log pagr************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.click_my_account()
        self.admin_lp.click_login()

        self.row = excel_utils.get_row_count(self.path, 'Sheet1')
        # print('number of rows' + self.row)

        for r in range(2, self.row + 1):
            self.username = excel_utils.read_data(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.read_data(self.path, 'Sheet1', r, 2)
            self.exp_login = excel_utils.read_data(self.path, 'Sheet1', r, 3)
            self.admin_lp.click_my_account()
            self.admin_lp.click_login()
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.login_button()

            actual_title = self.driver.title
            exp_title = "My Account"

            if actual_title == exp_title:
                if self.exp_login == "valid":
                    self.logger.info("Test data Passed")
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.exp_login == "invalid":
                    self.logger.info("Test data Failed")
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()
            elif actual_title != exp_title:
                if self.exp_login == "valid":
                    self.logger.info("Test data Failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "invalid":
                    self.logger.info("Test data Passed")
                    self.status_list.append("Pass")

        print('Status List is', self.status_list)

        if "invalid" in self.status_list:
            self.logger.info("Test admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is passed")
            assert True
