from selenium.webdriver.common.by import By
class LoginPage:
    click_yellow_button_login=(By.XPATH,"//a[@class='yellow-btn']")
    text_box_enter_number=(By.XPATH,"//input[@id='mobileNumber']")
    click_button_continue=(By.XPATH,"//button[@type='submit']")
    text_box_enter_password=(By.XPATH,"//input[@id='password']")
    click_button_login=(By.XPATH,"//button[@type='submit']")
    click_sample_bungalow = (By.XPATH, "//span[normalize-space()='Sample bungalow project']")
    click_detailed_estimate = (By.XPATH, "//p[@class='m-0 quote-title-web'][normalize-space()='Detailed Estimate']")

    def __init__(self,driver):
        self.driver=driver

    def ClickHomeLogin(self):
        self.driver.find_element(*self.click_yellow_button_login).click()

    def EnterNumber(self,number):
        self.driver.find_element(*self.text_box_enter_number).send_keys(number)

    def ClickContinue(self):
        self.driver.find_element(*self.click_button_continue).click()

    def EnterPassword(self,password):
        self.driver.find_element(*self.text_box_enter_password).send_keys(password)

    def Clicklogin(self):
        self.driver.find_element(*self.click_button_login).click()

    def bungalowProject(self):
        self.driver.find_element(*self.click_sample_bungalow).click()

    def detailedEstimates(self):
        self.driver.find_element(*self.click_detailed_estimate).click()


