from services.driver import Driver
from saucelab_android.pages.base_page import BasePage
from saucelab_android.pages.login_page import LoginPage
from saucelab_android.pages.catalog_page import CatalogPage

class PageFactory:
    def __init__(self, device):
        self.driver = Driver().set_up(device)
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)