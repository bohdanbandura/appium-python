from saucelab_android.pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def find_product(self, product_name):
        prev_products = []
        current_products = []
        found_product = False
        product_name = product_name.lower().strip()
        
        while product_name not in current_products:
            products = self.get_elements(self.catalog_page_locators.products)
            for product in products:
                text = self.get_text(self.catalog_page_locators.product_title, product).lower().strip()
                if(text != product_name):
                    current_products.append(text)
                else:
                    assert text == product_name, 'Product not found'
                    found_product = True
                    break
            
            if found_product: break
                
            if(prev_products == current_products):
                assert product_name in current_products, 'Product not found'
                break
            
            prev_products = current_products
            current_products = []
            self.scroll_page()
