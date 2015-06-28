from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")
    def test_Login(self):
        driver = self.driver
        facebookUsername = "alex.como@mail.ru"
        facebookPassword = "mariposa1282"


        emailFildID      = "email"
        passFieldID       = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath      = "(//a[contains(@href, 'logo')])[1]"
    

        emailFildElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFildID))
        passFieldElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonXpath))

        emailFildElement.clear()
        emailFildElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.cliick()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(fbLogoXpath))


    def tearDoen(self):
        self.driver.quit()
if __name__ == '__mine__':
    unittest.main()