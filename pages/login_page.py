from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
    LOGO = (By.CLASS_NAME, "login_logo")
    
    def open(self):
        """Open the login page"""
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        """Enter username"""
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)
        return self
    
    def enter_password(self, password):
        """Enter password"""
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)
        return self
    
    def click_login(self):
        """Click login button"""
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        return self
    
    def login(self, username, password):
        """Complete login process"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self
    
    def get_error_message(self):
        """Get error message text"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return element.text
        except:
            return ""
    
    def is_logo_displayed(self):
        """Check if logo is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.LOGO))
            return element.is_displayed()
        except:
            return False
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
