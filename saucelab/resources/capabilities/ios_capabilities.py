from typing import Any, Dict
import os

ios_file_name = "SauceLabs-Demo-App.ipa"

cap: Dict[str, Any] = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "deviceName": "iPhone.*",
    # "app": os.path.abspath(ios_file_name),
    "app": "storage:filename=SauceLabs-Demo-App.ipa",
    "sauce:options": {
        "username": "oauth-bohdan.bandura-b0e07",
        "accessKey": "606c7f0b-1dd8-48b9-a1b1-6d24de2dfa44",
        "build": "appium-build-MD3XG",
        "appiumVersion": "2.0.0"
    }
}