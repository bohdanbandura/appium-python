from appium import webdriver
from appium.options.common import AppiumOptions

from saucelab_android.resources.capabilities import cap as android_cap
from saucelab_ios.resources.capabilities import cap as ios_cap
from resources.appium_url import url


class Driver:
    def set_up(self, device):
        driver = None
    
        if(device == 'Android'):        
            driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(android_cap))
        elif(device == 'IOS'):
            driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(ios_cap))
            
        return driver