from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest
class RadioButtonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.aa.com/')
    def testButton(self):
        driver = self.driver
        oneWayID              = 'flightSearchForm.tripType.oneWay'
       # oneWayOnID            = 
        roundTripOffID        = 'flightSearchForm.tripType.roundTrip'
        roundTripHotelOffXpath   = "radio custombox-wrapper pillbox"
        
        oneWayElement         = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(oneWayID))
        roundTripElement      = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(roundTripOffID))
      #  roundTripHotelElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(roundTripHotelOffID))
        
        oneWayElement.click()
       # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_(aaLogoXpath))
       # WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_(aaLogoXpath))
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name()
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()