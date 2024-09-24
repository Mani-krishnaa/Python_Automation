from selenium.webdriver.common.by import By
from selenium import webdriver


class Login_Admin_page:
    textbox_username_xpath = "//input[@id='input-email']"
    textbox_password_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    my_account_xpath = "//span[normalize-space()='My Account']"
    my_login_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    my_logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self, driver):  # it is taking a driver and initializing to class variables
        self.driver = driver

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.my_login_xpath).click()

    def enter_username(self, userName):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath)
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(userName)

    def enter_password(self, passWord):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(passWord)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.my_logout_xpath).click()
