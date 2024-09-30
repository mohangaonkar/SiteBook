import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.QuotationPage import QuotationPage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
from testCases.test_Login import Test_001_Login

class Test_002_Quotation:

    logger = LogGen.loggen()

    @pytest.mark.dependency(depends=["test_login"])
    def test_quotation_sections(self, setup):
        self.logger.info("***** Validating Test_002_Quotation *****")

        self.driver = setup
        self.qp = QuotationPage(self.driver)

        self.logger.info("***** Waiting for exavation section *****")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.qp.exavation_section)
        )

        self.logger.info("***** fetching excavation detail *****")
        exavation_details = self.qp.get_exavation_details()

        expected_quantity_exavation = readconfig.get_quantity_exavation()
        expected_unit_exavation = readconfig.get_unit_exavation()
        expected_rate_exavation = readconfig.get_rate_exavation()

        self.logger.info(f"Expected Quantity: {expected_quantity_exavation}, "
                         f"Unit: {expected_unit_exavation}, "
                         f"Total Cost: {expected_rate_exavation}")

        if exavation_details[0] == expected_quantity_exavation:
            self.logger.info("********* Excavation quantity matched ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "excavation_quantity_mismatch.png")
            self.logger.error("******* Excavation quantity mismatched *********")


            self.driver.save_screenshot(".\\Screenshots\\" + "homepagetitle.png")

            # Validate unit
        if exavation_details[1] == expected_unit_exavation:
            self.logger.info("********* Excavation unit matched ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "excavation_unit_mismatch.png")
            self.logger.error("******* Excavation unit mismatched *********")


            # Validate rate
        if exavation_details[2] == expected_rate_exavation:
            self.logger.info("********* Excavation rate matched ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "excavation_rate_mismatch.png")
            self.logger.error("******* Excavation rate mismatched *********")

        try:
            element_locator = (By.XPATH, "//label[@class='name']")  # Adjust the XPath as needed
            self.logger.info("***** Waiting for the text element to be visible *****")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator))


            text = self.driver.find_element(*element_locator).text
            self.logger.info(f"Text from the element: {text}")

        except Exception as e:
            self.logger.error(f"An error occurred while retrieving text: {e}")
            self.driver.save_screenshot(".\\Screenshots\\" + "element_retrieve_error.png")
            assert False, f"Failed to retrieve text due to: {e}"


        self.logger.info("***** Test_003_Quotation Completed Successfully *****")
