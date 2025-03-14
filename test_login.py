import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    return LoginPage(driver)

def test_successful_login(login_page):
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    assert "dashboard" in login_page.driver.current_url

def test_invalid_login(login_page):
    login_page.enter_username("Admin")
    login_page.enter_password("invalid_password")
    login_page.click_login()
    assert login_page.get_error_message() == "Invalid credentials"