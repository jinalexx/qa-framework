import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def screenshot_on_failure(driver, request):
    yield
    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        driver.save_screenshot(f"reports/screenshots/{request.node.name}.png")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)