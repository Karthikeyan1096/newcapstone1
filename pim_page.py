from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.ID, "menu_pim_viewPimModule")
        self.add_employee_button = (By.ID, "btnAdd")
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.save_button = (By.ID, "btnSave")
        self.success_message = (By.CSS_SELECTOR, ".message.success")

    def go_to_pim_module(self):
        self.driver.find_element(*self.pim_menu).click()

    def click_add_employee(self):
        self.driver.find_element(*self.add_employee_button).click()

    def enter_employee_details(self, first_name, last_name):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text