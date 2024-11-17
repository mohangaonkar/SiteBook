from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuotationPage:

    exavation_section = (By.XPATH, "//span[normalize-space()='Excavation']")
    # backfilling_section = (By.XPATH, "//span[contains(text(),'Carrying out backfilling of plinth by machinery us')]")

    quantity_locator = (By.XPATH, "//tbody/tr[4]/td[3]")
    unit_locator = (By.XPATH, "//tbody/tr[4]/td[4]")
    total_cost_locator = (By.XPATH, "//tbody/tr[4]/td[5]")

    def __init__(self, driver):
        self.driver = driver

    def get_section_details(self, section_locator):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(section_locator))
        section_element = self.driver.find_element(*section_locator)

        quantity = section_element.find_element(*self.quantity_locator).text

        unit = section_element.find_element(*self.unit_locator).text

        total_cost = section_element.find_element(*self.total_cost_locator).text

        return quantity, unit, total_cost

    def get_exavation_details(self):
        return self.get_section_details(self.exavation_section)
