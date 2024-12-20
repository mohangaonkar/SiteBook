import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://mysitebook.io/")
    yield driver
    driver.quit()
