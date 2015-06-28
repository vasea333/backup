from datetime import date
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import AAHTML 
import random

class FlightTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.aa.com/")
    def test_Flight(self):
        driver = self.driver
        driver.maximize_window()
        trip = open("vacation.txt")
        for line in trip:
        words = line.split()
        originAirport        = words[0]
        leavingOn            = words[1]
        destinationAirport   = words[2]
        returningDay         = words[3]

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
        Select(passengerCountDropD).select_by_visible_text(words[4]+" Travelers")
        time.sleep(1)
        submitButtonElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(aaLogoXpath))

    def alexRusu(self):
        self.driver.quit()
if __name__ == '__main__':
    AAHTML.main()