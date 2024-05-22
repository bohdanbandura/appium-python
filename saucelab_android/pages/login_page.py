from saucelab_android.pages.base_page import BasePage
from saucelab_android.resources.test_data import TestData

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def login(self, email, password):
        self.open_login_page()
        self.input_text(self.login_page_locators.email, email)
        self.input_text(self.login_page_locators.password, password)
        self.click_element(self.login_page_locators.login_btn)
        if (email == TestData.wrong_email):
            err = self.get_text(self.login_page_locators.login_err)
            assert err == 'Sorry this user has been locked out.', 'The wrong msg is displayed'