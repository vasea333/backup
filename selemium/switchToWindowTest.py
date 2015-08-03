import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class FlightTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.popuptest.com/")
    def test_Flight(self):
        driver = self.driver
        driver.maximize_window()

        MultiPopUpXpath          = "(//a[contains(@href, 'popuptest2.html')])"
        LogoXpath  = ('//body[@bgcolor="#3D59AB"]')

        MultiPopUpElement        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(MultiPopUpXpath))

        MultiPopUpElement.click()
        driver.window_handles
        driver.switch_to_window()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(LogoXpath))





    def alexRusu(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()