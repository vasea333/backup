from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import AAHTML

class FlightTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.aa.com/")
    def test_Flight(self):
        driver = self.driver
        driver.maximize_window()
        originAirport        = "SFO"
        leavingOn            = "12/23/2014"
        destinationAirport   = "LAS"
        returningDay         = "12/24/2014"

        originAirportID      = "reservationFlightSearchForm.originAirport"
        leavingOnID          = "aa-leavingOn"
        destinationAirportID = "reservationFlightSearchForm.destinationAirport"
        returningDayID       = "aa-returningFrom"
        submitButtonID       = "flightSearchForm.button.reSubmit"
        passengerCountID       = "flightSearchForm.adultOrSeniorPassengerCount"
        aaLogoXpath          = "(//a[contains(@href, '/homePage.do')])"

        originAirportElement      = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(originAirportID))
        leavingOnElement          = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(leavingOnID))
        destinationAirportElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(destinationAirportID))
        returningDayElement       = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(returningDayID))
        submitButtonElement       = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(submitButtonID))
        passengerCountDropD       = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passengerCountID))

        originAirportElement.clear()
        originAirportElement.send_keys(originAirport)
        leavingOnElement.clear()
        leavingOnElement.send_keys(leavingOn)
        destinationAirportElement.clear()
        destinationAirportElement.send_keys(destinationAirport)
        returningDayElement.clear()
        returningDayElement.send_keys(returningDay)
        Select(passengerCountDropD).select_by_visible_text("2 Travelers")
        time.sleep(1)
        submitButtonElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(aaLogoXpath))


    def alexRusu(self):
        self.driver.quit()
if __name__ == '__main__':
    AAHTML.main()

