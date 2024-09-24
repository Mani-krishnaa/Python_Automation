import pytest

from base_pages.Registration_Page import Registration_page
from test_cases.conftest import random_alpha_string
from test_cases.conftest import random_number
from test_cases.conftest import random_string
from utilities.Custom_Logging import Log_Maker
from utilities.read_properties import Read_config


class Test_03_Admin_Registration:
    admin_page_url = Read_config.get_admin_page_url()
    # username = Read_config.get_username()
    # password = Read_config.get_password()
    logger = Log_Maker.log_gen()
    Password = random_alpha_string()

    @pytest.mark.regression
    def test_registration(self, setup):
        self.logger.info("*********test_registration************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_rc = Registration_page(self.driver)
        self.admin_rc.my_account()
        self.admin_rc.my_register()
        self.logger.info("*********new registration will start************")

        self.admin_rc.first_Name(random_string())
        self.admin_rc.last_Name(random_string())
        self.admin_rc.email(random_string() + '@gmail.com')
        self.admin_rc.telephone(random_number())
        self.admin_rc.password(self.Password)
        self.admin_rc.conf_password(self.Password)
        self.admin_rc.agree()
        self.admin_rc.Continue()

        confirmationMessage = self.admin_rc.confirm_message()
        if confirmationMessage == "Your Account Has Been Created!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("/home/manikrishna/Pycharm/Python_Automation/screenshots/failure.png")
            self.driver.close()
            assert False
