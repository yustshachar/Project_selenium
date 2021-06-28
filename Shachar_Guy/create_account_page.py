from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class create_account_page:
    def __init__(self, driver):
        self.driver = driver

    def fiil_username_field(self, username):
        self.driver.find_element_by_name('usernameRegisterPage').send_keys(username)

    def fiil_email_field(self, email):
        self.driver.find_element_by_name('emailRegisterPage').send_keys(email)

    def fiil_password_field(self, password):
        self.driver.find_element_by_name('passwordRegisterPage').send_keys(password)

    def fiil_confirm_password_field(self, password):
        self.driver.find_element_by_name('confirm_passwordRegisterPage').send_keys(password)

    def i_agree_checkbox(self):
        return self.driver.find_element_by_name("i_agree")

    def i_agree_checkbox_click(self):
        element = self.driver.find_element_by_name("i_agree")
        self.driver.execute_script("arguments[0].click();", element)

    def register_button(self):
        return self.driver.find_element_by_id("register_btnundefined")

    def register_button_click(self):
        element = self.register_button()
        self.driver.execute_script("arguments[0].click();", element)