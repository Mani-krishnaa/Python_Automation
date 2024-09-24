import string
import random as rnd

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # return driver

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser not supported! Choose from: chrome, firefox, edge.")
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope='function', autouse=True)
def browser(request):
    return request.config.getoption("--browser")


from pytest_metadata.plugin import metadata_key


###beloww is the peace  of code called hooks to addd custom reports  iin html

# hooks for adding info to HTML reports
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project, Qarof.com'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'ManiKrishna'


# hooks for deleting/modifying environment info in html reports
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


def random_string():
    """Generates a random alphabetic string of 5 characters."""
    return ''.join(rnd.choices(string.ascii_letters, k=5))  # Random alphabetic string of length 5


def random_number():
    """Generates a random numeric string of 10 digits."""
    return ''.join(rnd.choices(string.digits, k=10))  # Random numeric string of length 10


def random_alpha_string():
    """Generates a random string consisting of 5 alphabetic characters followed by 10 numeric characters."""
    return f"{random_string()}@{random_number()}"

# # Example usage
# print(f"Random String: {random_string()}")
# print(f"Random Number: {random_number()}")
# print(f"Random Alpha String: {random_alpha_string()}")
