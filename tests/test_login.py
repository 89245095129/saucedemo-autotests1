import pytest
import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@allure.feature("Login Tests")
@allure.story("Authentication")
class TestLogin:
    
    @allure.title("Successful login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, login_page, products_page):
        """Test successful login with standard_user"""
        with allure.step("Enter valid credentials"):
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Verify URL changed to inventory page"):
            assert "inventory" in products_page.get_current_url()
        
        with allure.step("Verify products page is displayed"):
            assert products_page.get_title() == "Products"
            assert products_page.is_products_container_displayed() is True
            assert products_page.is_shopping_cart_displayed() is True
    
    @allure.title("Login with invalid password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_password(self, login_page):
        """Test login with wrong password"""
        with allure.step("Enter invalid password"):
            login_page.login("standard_user", "wrong_password")
        
        with allure.step("Verify error message is displayed"):
            error_message = login_page.get_error_message()
            assert "Username and password do not match" in error_message
        
        with allure.step("Verify still on login page"):
            assert "saucedemo.com" in login_page.get_current_url()
            assert login_page.is_logo_displayed() is True
    
    @allure.title("Login with locked out user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_out_user(self, login_page):
        """Test login with locked_out_user"""
        with allure.step("Enter locked out user credentials"):
            login_page.login("locked_out_user", "secret_sauce")
        
        with allure.step("Verify locked out error message"):
            error_message = login_page.get_error_message()
            assert "Sorry, this user has been locked out" in error_message
        
        with allure.step("Verify still on login page"):
            assert "saucedemo.com" in login_page.get_current_url()
    
    @allure.title("Login with empty fields")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_fields(self, login_page):
        """Test login with empty username and password"""
        with allure.step("Click login without entering credentials"):
            login_page.click_login()
        
        with allure.step("Verify error message for empty fields"):
            error_message = login_page.get_error_message()
            assert "Username is required" in error_message
        
        with allure.step("Verify still on login page"):
            assert "saucedemo.com" in login_page.get_current_url()
    
    @allure.title("Login with performance glitch user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_performance_glitch_user(self, login_page, products_page):
        """Test login with performance_glitch_user"""
        with allure.step("Enter performance glitch user credentials"):
            login_page.login("performance_glitch_user", "secret_sauce")
        
        with allure.step("Verify successful login despite delays"):
            # Add explicit wait for slower loading
            import time
            time.sleep(3)  # Allow time for potential delays
            
            assert "inventory" in products_page.get_current_url()
            assert products_page.is_products_container_displayed() is True
            assert products_page.get_title() == "Products"
