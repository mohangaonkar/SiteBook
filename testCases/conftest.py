import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Edge()  # or Firefox, depending on your setup
    driver.maximize_window()
    driver.get("https://mysitebook.io/")  # login page
    yield driver
    driver.quit()
