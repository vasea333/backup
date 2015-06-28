from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
class AndysTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.andys.md/en/main.html")
    def test_signIn(self):
        driver = self.driver
        driver.maximize_window()
        trip = open("NamePass.txt")
        for line in trip:
            words = line.split()
        email         = words[0]
        password      = words[1]
        
        singInbuttonCSS     ='#mainwrapper.mainwrapper div.header div.topmenu.cl div.s2.cl div.regsigncick'
        emailXpath          ='html/body/div[1]/div/div[1]/div/div[2]/form/div[2]/input'
        passwordXpath       ='html/body/div[1]/div/div[1]/div/div[2]/form/div[4]/input'
        singInbuttonXpath   ='html/body/div[1]/div/div[1]/div/div[2]/form/div[5]/input'
        singInButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(singInbuttonCSS))
        singInButtonElement.click()
        emailElement        = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailXpath))
        passwordElement     = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passwordXpath))
        singInbuttonXpathElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(singInbuttonXpath))
        emailElement.send_keys(email)        
        passwordElement.send_keys(password)
        singInbuttonXpathElement.click()
    def dtearDown(self):
        self.driver.quit()
        
if __name__=='__main':
    unittest.main|()
    

       
    