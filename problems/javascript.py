from selenium import webdriver
import unittest

class JavascriptTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://jqueryui.com/slider/")
    def test_Javascript(self):
        driver = self.driver
        driver.execute_script("$('#slider').slider('option','value',80)")
              
    def alexRusu(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()