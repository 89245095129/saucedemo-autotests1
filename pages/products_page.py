from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS_CONTAINER = (By.CLASS_NAME, "inventory_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    
    def get_title(self):
        """Get page title text"""
        element = self.wait.until(EC.visibility_of_element_located(self.TITLE))
        return element.text
    
    def is_products_container_displayed(self):
        """Check if products container is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_CONTAINER))
            return element.is_displayed()
        except:
            return False
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def logout(self):
        """Logout from the application"""
        # Open menu
        menu_button = self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON))
        menu_button.click()
        
        # Click logout
        logout_link = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))
        logout_link.click()
        
    def is_shopping_cart_displayed(self):
        """Check if shopping cart is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART))
            return element.is_displayed()
        except:
            return False
