import pytest
import allure
import sys

# Выбираем драйвер в зависимости от ситуации
try:
    from utils.driver import DriverFactory
    DRIVER_SOURCE = "driver"
except:
    try:
        from utils.simple_driver_fixed import FixedDriver
        DRIVER_SOURCE = "fixed"
    except:
        DRIVER_SOURCE = "direct"

@pytest.fixture
def driver():
    """Create WebDriver instance for Python 3.14"""
    print(f"Python version: {sys.version}")
    print(f"Using driver source: {DRIVER_SOURCE}")
    
    if DRIVER_SOURCE == "driver":
        driver_instance = DriverFactory.get_driver("chrome")
    elif DRIVER_SOURCE == "fixed":
        driver_instance = FixedDriver.get_driver()
    else:
        # Экстренный вариант
        from selenium import webdriver
        driver_instance = webdriver.Chrome()
    
    yield driver_instance
    
    # Закрытие драйвера
    try:
        driver_instance.quit()
    except:
        pass

# Остальной код без изменений...
@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver).open()

@pytest.fixture
def products_page(driver):
    from pages.products_page import ProductsPage
    return ProductsPage(driver)
