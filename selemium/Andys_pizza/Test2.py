from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from lib2to3.tests.support import driver
class AndysTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.andys.md/en/main.html")
    def test_signIn(self):
        driver = self.driver
        driver.maximize_window()
        singInbuttonXpath   ='#mainwrapper.mainwrapper div.header div.topmenu.cl div.s2.cl div.regsigncick'
        singInButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(singInbuttonXpath))
        singInButtonElement.click()
    #def tearDown(self):
        #self.driver.quit()
if __name__=='__main':
    unittest.main|()