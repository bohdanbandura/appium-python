from appium.webdriver.common.appiumby import AppiumBy

class BasePageLocators:
    def __init__(self):
        self.burger_menu = (AppiumBy.ACCESSIBILITY_ID, 'View menu')
        self.login_btn = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/itemTV" and @text="Log In"]')
        
        
class LoginPageLocators:
    def __init__(self):
        self.email = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/nameET"]')
        self.password = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/passwordET"]')
        self.login_btn = (AppiumBy.ACCESSIBILITY_ID, 'Tap to login with given credentials')
        self.login_err = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/passwordErrorTV"]')
        

class CatalogPageLocators:
    def __init__(self):
        self.products = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup')
        self.product_title = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/titleTV"]')