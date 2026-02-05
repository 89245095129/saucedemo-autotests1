import pytest
import allure
from utils.driver import DriverFactory

@pytest.fixture
def driver():
    """Create WebDriver instance"""
    driver = DriverFactory.get_driver("chrome")
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    """Create LoginPage instance"""
    from pages.login_page import LoginPage
    return LoginPage(driver).open()

@pytest.fixture
def products_page(driver):
    """Create ProductsPage instance"""
    from pages.products_page import ProductsPage
    return ProductsPage(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Create screenshot on test failure"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs["driver"]
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
