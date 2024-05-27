from appium import webdriver
from appium.options.common import AppiumOptions

from saucelab.resources.capabilities.android_capabilities import cap as android_cap
from saucelab.resources.capabilities.ios_capabilities import cap as ios_cap
from saucelab.resources.appium_url import url


class Driver:
    
    @staticmethod
    def set_up(device: str) -> webdriver.Remote:
        driver = None
    
        if device == 'android':        
            driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(android_cap))
        else:
            driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(ios_cap))
            
        return driver