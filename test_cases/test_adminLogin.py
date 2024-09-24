import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_page import Login_Admin_page
from utilities.read_properties import Read_config
from utilities.Custom_Logging import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    invalid_password = Read_config.get_invalid_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.skip
    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        acual_title = self.driver.title
        expeted_title = "Your Store"
        if acual_title == expeted_title:
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_valid_admin_login(self, setup):
        self.logger.info("*********test_valid_admin_login************")
        self.logger.info("*********Verificatin of admin log pagr************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.click_my_account()
        self.admin_lp.click_login()
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.login_button()
        act_dashBard_text = self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Account']").text
        if act_dashBard_text == "My Account":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.xfail
    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.click_my_account()
        self.admin_lp.click_login()
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.invalid_username)
        self.admin_lp.login_button()
        error_message = self.driver.find_element(By.XPATH,
                                                 "//div[@class='alert alert-danger alert-dismissible']").text
        if error_message == "Warning: No match for E-Mail Address and/or Password.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/manikrishna/Pycharm/Python_Automation/screenshots/failure.png")
            self.driver.close()
            assert False
