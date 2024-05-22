from typing import Any, Dict
import os

file_name = "mda-2.0.1-22.apk"

cap: Dict[str, Any] = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "deviceName": "Android",
    "appPackage": "com.saucelabs.mydemoapp.android",
    "language": "en",
    "locale": "US",
    "app": os.path.abspath(file_name)
}