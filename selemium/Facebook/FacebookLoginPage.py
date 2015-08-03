from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest
import FacebookHTML

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")
    def test_Login(self):
        driver = self.driver
        facebookUsername = "username"
        facebookPassword = "pass"


        emailFieldID      = "email"
        passFieldID       = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath      = "(//a[contains(@href, 'logo')])[1]"

        emailFildElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFildElement.clear()
        emailFildElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))


    def tearDoen(self):
        self.driver.quit()
if __name__ == '__main__':
    FacebookHTML.main()

