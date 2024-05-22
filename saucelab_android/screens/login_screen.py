from saucelab_android.screens.base_screen import BaseScreen
from saucelab_android.resources.test_data import TestData

class LoginScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)
        
    def login(self, email, password):
        self.open_login_screen()
        self.input_text(self.login_screen_locators.email, email)
        self.input_text(self.login_screen_locators.password, password)
        self.click_element(self.login_screen_locators.login_btn)
        if (email == TestData.wrong_email):
            err = self.get_text(self.login_screen_locators.login_err)
            assert err == 'Sorry this user has been locked out.', 'The wrong msg is displayed'