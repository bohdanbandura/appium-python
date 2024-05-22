import allure
from appium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from saucelab_android.resources.locators import LoginScreenLocators
from saucelab_android.resources.locators import BaseScreenLocators
from saucelab_android.resources.locators import CatalogScreenLocators

class BaseScreen:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.base_screen_locators = BaseScreenLocators()
        self.login_screen_locators = LoginScreenLocators()
        self.catalog_screen_locators = CatalogScreenLocators()
        self.wait = WebDriverWait(self.driver, 10)
        
    @allure.step('Get element {locator}')
    def get_element(self, locator: str, el: WebElement = None):
        if(el is not None):
            return el.find_element(*locator)
        else:
            return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Get elements {locator}')
    def get_elements(self, locator):        
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    @allure.step('Click on element {locator}')
    def click_element(self, locator, el: WebElement = None):
        self.get_element(locator, el).click()
        
    @allure.step('Type in element {locator}')
    def input_text(self, locator, text, el: WebElement = None):
        self.get_element(locator, el).send_keys(text)
        
    @allure.step('Get text from element {locator}')
    def get_text(self, locator, el: WebElement = None):
        return self.get_element(locator, el).text
    
    @allure.step('Scroll screen')
    def scroll_screen(self):
        device_size = self.driver.get_window_size()
        screen_height = device_size['height']
        screen_width = device_size['width']
        startY = screen_height * 8 / 9
        endY = screen_height / 9
        startX =  screen_width / 2
        endX = screen_width / 2
        self.driver.swipe(start_x=startX, start_y=startY, end_x=endX, end_y=endY, duration=1000)
        
    @allure.step('Open login screen')
    def open_login_screen(self):
        self.click_element(self.base_screen_locators.burger_menu)
        self.click_element(self.base_screen_locators.login_btn)
