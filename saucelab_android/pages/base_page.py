import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from saucelab_android.resources.locators import LoginPageLocators
from saucelab_android.resources.locators import BasePageLocators
from saucelab_android.resources.locators import CatalogPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.device_size = self.driver.get_window_size()
        self.screen_height = self.device_size['height']
        self.screen_width = self.device_size['width']
        self.startY = self.screen_height * 8 / 9
        self.endY = self.screen_height / 9
        self.startX =  self.screen_width / 2
        self.endX = self.screen_width / 2
        self.base_page_locators = BasePageLocators()
        self.login_page_locators = LoginPageLocators()
        self.catalog_page_locators = CatalogPageLocators()
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
    
    @allure.step('Scroll page')
    def scroll_page(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
        actions.w3c_actions.pointer_action.move_to_location(self.startX, self.startY)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(self.endX, self.endY)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    @allure.step('Open login page')
    def open_login_page(self):
        self.click_element(self.base_page_locators.burger_menu)
        self.click_element(self.base_page_locators.login_btn)
