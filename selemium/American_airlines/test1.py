from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
class RadioButtonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.aa.com/')
    def testButton(self):
        driver = self.driver
        oneWayID              = 'html/body/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/form/div[1]/ul/li[2]/label'
        oneWayElement         = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(oneWayID))
        oneWayElement.click()
               
       
    def AtearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()