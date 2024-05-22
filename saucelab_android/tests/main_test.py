import pytest
import allure

from saucelab_android.resources.test_data import TestData

@allure.feature('Main')
@pytest.mark.usefixtures("pages")
class TestMain:
    
    @allure.story('Positive login')
    def test_positive_login(self, pages):
        login_page = pages.login_page
        login_page.login(TestData.email, TestData.password)
        
    @allure.story('Negative login')
    def test_negative_login(self, pages):
        login_page = pages.login_page
        login_page.login(TestData.wrong_email, TestData.password)
        
    @allure.story('Find existing product')
    def test_find_product(self, pages):
        catalog_page = pages.catalog_page
        catalog_page.find_product(TestData.product_name)
        
    @allure.story('Find non existing product')
    def test_negative_find_product(self, pages):
        catalog_page = pages.catalog_page
        catalog_page.find_product(TestData.wrong_product_name)