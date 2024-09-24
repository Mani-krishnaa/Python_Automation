from selenium.webdriver.common.by import By


class Home_page:
    searchBox_xpath = '//input[@placeholder="Search"]'
    searchButton_xpath = '//button[@class="btn btn-default btn-lg"]'
    iphone_xpath = "//div[@class='caption']//a[contains(text(),'iPhone')]"

    def __init__(self, driver):
        self.driver = driver

    def search_box(self, text):
        self.driver.find_element(By.XPATH, self.searchBox_xpath).send_keys(text)

    def search_button(self):
        self.driver.find_element(By.XPATH, self.searchButton_xpath).click()

    def iphone_present_or_not(self):
        element = self.driver.find_element(By.XPATH, self.iphone_xpath)
        return element.is_displayed()
