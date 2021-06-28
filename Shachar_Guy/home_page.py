from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class home_page:
    def __init__(self, driver):
        self.driver=driver

    def category(self, name):
        return self.driver.find_element_by_id(f"{name}Img")

    def click_category(self, name):
        self.category(name).click()

    def user_miniTitle(self):
        sleep(1)
        return self.driver.find_element_by_css_selector(".containMiniTitle")

    def user_miniTitle_text(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".containMiniTitle")))
        miniTitle = self.user_miniTitle()
        return miniTitle.text

    def nav_userIcon_click(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[class="PopUp"]')))
        self.driver.find_element_by_id('menuUser').click()

    def fill_username_field(self, input):
        self.driver.find_element_by_name('username').send_keys(input)

    def fill_password_field(self, input):
        self.driver.find_element_by_name('password').send_keys(input)

    def click_signIn_button(self):
        self.driver.find_element_by_id("sign_in_btnundefined").click()

    def click_signOut_button(self):
        self.driver.find_element_by_css_selector('[class="option roboto-medium ng-scope"][translate="Sign_out"]').click()