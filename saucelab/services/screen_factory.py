from saucelab.services.driver import Driver
from saucelab.screens.base_screen import BaseScreen
from saucelab.screens.login_screen import LoginScreen
from saucelab.screens.catalog_screen import CatalogScreen

class ScreenFactory:
    def __init__(self, device: str):
        self.driver = Driver().set_up(device)
        self.base_screen = BaseScreen(self.driver, device)
        self.login_screen = LoginScreen(self.driver, device)
        self.catalog_screen = CatalogScreen(self.driver, device)