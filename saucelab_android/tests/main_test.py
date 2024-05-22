import pytest
import allure

from saucelab_android.resources.test_data import TestData

@allure.feature('Main')
@pytest.mark.usefixtures("screens")
class TestMain:
    
    @allure.story('Positive login')
    def test_positive_login(self, screens):
        login_screen = screens.login_screen
        login_screen.login(TestData.email, TestData.password)
        
    @allure.story('Negative login')
    def test_negative_login(self, screens):
        login_screen = screens.login_screen
        login_screen.login(TestData.wrong_email, TestData.password)
        
    @allure.story('Find existing product')
    def test_find_product(self, screens):
        catalog_screen = screens.catalog_screen
        catalog_screen.find_product(TestData.product_name)
        
    @allure.story('Find non existing product')
    def test_negative_find_product(self, screens):
        catalog_screen = screens.catalog_screen
        catalog_screen.find_product(TestData.wrong_product_name)