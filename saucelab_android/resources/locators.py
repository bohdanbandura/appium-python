from appium.webdriver.common.appiumby import AppiumBy

class BaseScreenLocators:
    burger_menu = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/menuIV")')
    login_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log In")')  
        
class LoginScreenLocators:
    email = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/nameET")')
    password = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/passwordET")')
    login_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/loginBtn")')
    login_err = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/passwordErrorTV")')
        
class CatalogScreenLocators:
    products = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup")')
    product_title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.saucelabs.mydemoapp.android:id/titleTV")')
