from appium.webdriver.common.appiumby import AppiumBy

class IOSBaseScreenLocators:
    burger_menu = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "More-tab-item"`]')
    login_btn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "LogOut-menu-item"`]')
    
class IOSLoginScreenLocators:
    email = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    password = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
    login_btn = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Login"`]')
    login_err = (AppiumBy.IOS_CLASS_CHAIN, '')
        
class IOSCatalogScreenLocators:
    products = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Catalog-screen"`]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell')
    product_title = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText')