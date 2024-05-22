from services.driver import Driver
from saucelab_android.screens.base_screen import BaseScreen
from saucelab_android.screens.login_screen import LoginScreen
from saucelab_android.screens.catalog_screen import CatalogScreen

class ScreenFactory:
    def __init__(self, device: str):
        self.driver = Driver().set_up(device)
        self.base_screen = BaseScreen(self.driver)
        self.login_screen = LoginScreen(self.driver)
        self.catalog_screen = CatalogScreen(self.driver)