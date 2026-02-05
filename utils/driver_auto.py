from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

try:
    from webdriver_manager.chrome import ChromeDriverManager
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False
    print(" webdriver-manager не установлен")

class AutoDriver:
    @staticmethod
    def get_driver():
        """Автоматическая установка ChromeDriver"""
        options = Options()
        options.add_argument("--start-maximized")
        
        if WEBDRIVER_MANAGER_AVAILABLE:
            print(" Использую webdriver-manager...")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            print(" Использую стандартный драйвер...")
            driver = webdriver.Chrome(options=options)
        
        driver.implicitly_wait(10)
        return driver
