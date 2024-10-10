import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Login import  LoginPage
from Utilities.readProperties import readconfig
from Utilities.customLogger import Log_Class

class Test_001_Login:


    baseURL=readconfig.appURL()
    usernumber=readconfig.Usernumber()
    password=readconfig.Password()

    logger = Log_Class.log_generator()

    @pytest.mark.dependency(name="test_login")
    def test_login(self,setup):
        self.logger.info("***** Validating: Test_001_Login *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.logger.info("***** Opening the base URL *****")
        self.driver.get(self.baseURL)

        try:
            self.logger.info("***** Waiting for the popup close button to appear *****")
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//img[@src='https://mysitebook.io/wp-content/themes/mysitebook/assets/images/knowledge/close.svg']"))

            )
            close_button.click()
            self.logger.info("***** Popup closed successfully *****")

        except Exception as e:
            self.logger.error(f"***** Popup close failed:{e} *****")

        self.logger.info("***** Initiating login process *****")
        self.lp = LoginPage(self.driver)

        self.logger.info("***** Clicking Home login button *****")
        self.lp.ClickHomeLogin()

        all_tabs=self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
        self.logger.info("***** Switched to new tab *****")

        title=self.driver.title
        self.logger.info(f"***** Page title after switching tab:{title} *****")

        self.logger.info("***** Entering usrname *****")
        self.lp.EnterNumber(self.usernumber)

        self.logger.info("***** clicking continue button *****")
        self.lp.ClickContinue()

        self.logger.info("***** Entering password *****")
        self.lp.EnterPassword(self.password)

        self.logger.info("***** clicking on login button *****")
        self.lp.Clicklogin()

        time.sleep(5)
        titleLogin=self.driver.title
        self.logger.info(f"***** Page title after login:{titleLogin} *****")

        assert "Projects | Active" in titleLogin, "Login Failed"
        self.logger.info("***** Login successful,navigating to Projects *****")

        self.logger.info("***** Waiting for sample bungalow link *****")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.lp.click_sample_bungalow)
        )

        self.logger.info("***** clicking on sample bungalow project *****")
        self.lp.bungalowProject()

        self.logger.info("***** Waiting for detailed estimate link *****")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.lp.click_detailed_estimate)
        )

        self.logger.info("***** clicking detailed estimate link *****")
        self.lp.detailedEstimates()

        title_estimates = self.driver.title
        self.logger.info(f"***** Title at detailed estimates: {title_estimates} *****")
        self.logger.info("***** Test_001_Login completed *****")





