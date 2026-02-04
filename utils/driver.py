from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        """Create and return WebDriver instance"""
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run in background
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver
