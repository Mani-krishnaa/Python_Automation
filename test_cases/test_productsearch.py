import time

import pytest

from base_pages.Login_Admin_page import Login_Admin_page
from utilities.Custom_Logging import Log_Maker
from utilities.read_properties import Read_config
from base_pages.Home_page import Home_page


class Test_04_Product_search:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    product = Read_config.get_product()
    logger = Log_Maker.log_gen()
    @pytest.mark.regression
    def test_productSearch(self, setup):
        self.driver = setup
        self.logger.info("*********test_valid_admin_login************")
        self.logger.info("*********Verificatin of admin log pagr************")
        self.driver.get(self.admin_page_url)
        
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.click_my_account()
        self.admin_lp.click_login()
        
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.login_button()
        
        self.Home_page = Home_page(self.driver)
        self.Home_page.search_box(self.product)
        self.Home_page.search_button()

        text = self.Home_page.iphone_present_or_not()
        assert text, "iPhone should be present on the page"
