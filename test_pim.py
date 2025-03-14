import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    return LoginPage(driver)

@pytest.fixture(scope="module")
def pim_page(driver, login_page):
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    return PIMPage(driver)

def test_add_employee(pim_page):
    pim_page.go_to_pim_module()
    pim_page.click_add_employee()
    pim_page.enter_employee_details("John", "Doe")
    pim_page.click_save()
    assert pim_page.get_success_message() == "Successfully Saved"