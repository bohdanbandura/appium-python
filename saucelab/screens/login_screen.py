from saucelab.screens.base_screen import BaseScreen
from saucelab.resources.test_data import TestData

class LoginScreen(BaseScreen):
    def __init__(self, driver, device):
        super().__init__(driver, device)
        
    def login(self, email, password):
        self.open_login_screen()
        self.input_text(self.login_screen_locators.email, email)
        self.input_text(self.login_screen_locators.password, password)
        self.click_element(self.login_screen_locators.login_btn)
        self.driver.hide_keyboard()
        if (email == TestData.wrong_email):
            err = self.get_text(self.login_screen_locators.login_err)
            assert err == 'Sorry this user has been locked out.', 'The wrong msg is displayed'
        