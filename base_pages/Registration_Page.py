from selenium.webdriver.common.by import By


class Registration_page:
    my_account_xpath = "//span[normalize-space()='My Account']"
    register_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']"

    firstName_xpath = "//input[@id='input-firstname']"
    lastName_xpath = "//input[@id='input-lastname']"
    email_xpath = "//input[@id='input-email']"
    telephone_xpath = "//input[@id='input-telephone']"
    password_xpath = "//input[@id='input-password']"
    passwordConfirm_xpath = "//input[@id='input-confirm']"
    newsletter_xpath = "//input[@value='0']"
    agree_xpath = "//input[@name='agree']"
    Continue_xpath = "//input[@value='Continue']"
    confirm_message_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def my_register(self):
        self.driver.find_element(By.XPATH, self.register_xpath).click()

    def first_Name(self, name):
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(name)

    def last_Name(self, name):
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(name)

    def email(self, mail):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(mail)

    def telephone(self, num):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(num)

    def password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def conf_password(self, password):
        self.driver.find_element(By.XPATH, self.passwordConfirm_xpath).send_keys(password)

    def agree(self):
        self.driver.find_element(By.XPATH, self.agree_xpath).click()

    def Continue(self):
        self.driver.find_element(By.XPATH, self.Continue_xpath).click()

    def confirm_message(self):
        try:
            element = self.driver.find_element(By.XPATH, self.confirm_message_xpath)
            return element.text
        except Exception as e:
            # Handle any other unexpected exceptions
            return f"An unexpected error occurred: {str(e)}"
