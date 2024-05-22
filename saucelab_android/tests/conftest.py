import pytest
import os
import allure
from allure_commons.types import AttachmentType
from datetime import datetime

from saucelab_android.services.screen_factory import ScreenFactory

@pytest.fixture()
def screens(request):
    screen_factory = ScreenFactory('Android')
    driver = screen_factory.driver
    yield screen_factory
    item = request.node
    folder_path = './saucelab_android/failed_screenshots'
    if item.rep_call.failed:
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        screenshot_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'
        driver.save_screenshot(f'{folder_path}/{item.name}_{screenshot_name}')
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)
    driver.quit()
    
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep