from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        """Create and return WebDriver instance for Python 3.14"""
        if browser.lower() == "chrome":
            # Новый способ для Chrome версий 115+
            options = Options()
            
            # Убираем устаревшие аргументы
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            
            # Для Python 3.14 и новых версий Chrome
            # options.add_argument("--headless=new")  # Закомментируйте пока
            
            # Отключаем автоматизацию-детект
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            try:
                # Автоматическое управление драйвером
                service = Service(
                    ChromeDriverManager(
                        chrome_type=ChromeType.GOOGLE
                    ).install()
                )
                
                driver = webdriver.Chrome(service=service, options=options)
                driver.implicitly_wait(10)
                
                # Убираем сообщение "Chrome is being controlled..."
                driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                    'source': '''
                        Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                        });
                    '''
                })
                
                return driver
                
            except Exception as e:
                print(f"Ошибка Chrome WebDriver: {e}")
                print("Пробуем Firefox...")
                return DriverFactory.get_driver("firefox")
                
        elif browser.lower() == "firefox":
            # Альтернатива: Firefox
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            
            options = FirefoxOptions()
            # options.add_argument("--headless")  # Закомментируйте
            
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            driver.implicitly_wait(10)
            return driver
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
