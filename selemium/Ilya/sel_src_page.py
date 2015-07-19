from element import BasePageElement
from locators import LoginPageLocators
from locators import MainViewPageLocators
from utils import SmartSearch


class SearchTextElement(BasePageElement):

    locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.smart_driver = SmartSearch(self.driver)


class LoginPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "File Server" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

    def put_text_to_username_field(self, text):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)
        element.send_keys(text)

    def put_text_to_password_field(self, text):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys(text)

    def login(self):
        self.put_text_to_username_field('istepanko')
        self.put_text_to_password_field('egnyte4you')
        self.click_login_button()


class MainViewPage(BasePage):

    def is_title_matches(self):
        return "/Shared" in self.driver.title

    def create_folder(self, name):
        element = self.smart_driver.smart_find(*MainViewPageLocators.NEW_FOLDER_BUTTON)
        element.click()
        element = self.smart_driver.smart_find(*MainViewPageLocators.CREATE_FOLDER_FIELD)
        element.send_keys(name)
        element = self.smart_driver.smart_find(*MainViewPageLocators.CREATE_FOLDER_BUTTON)
        element.click()

    def get_message_text(self):
        return self.smart_driver.smart_find(*MainViewPageLocators.MESSAGE).text

"""
class SearchResultsPage(BasePage):

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
"""