from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class payment_page:
    def __init__(self, driver):
        self.driver = driver

    def choose_credit_card(self):
        self.driver.find_element_by_name("masterCredit").click()

    def card_number(self):
        return self.driver.find_element_by_id("creditCard")

    def cvv(self):
        return self.driver.find_element_by_name("cvv_number")

    def cardholder_name(self):
        return self.driver.find_element_by_name("cardholder_name")

    def choose_mm(self, mm):
        Select(self.driver.find_element_by_name("mmListbox")).select_by_visible_text(f"{mm}")

    def choose_yyyy(self, yyyy):
        Select(self.driver.find_element_by_name("yyyyListbox")).select_by_visible_text(f"{yyyy}")

    def save_card_to_user(self):
        self.driver.find_element_by_name("save_master_credit").click()

    def pay_now_button(self):
        return self.driver.find_element_by_id("pay_now_btn_ManualPayment")

    def pay_now_button_click(self):
        self.pay_now_button().click()

    def order_number(self):
        return self.driver.find_element_by_id("orderNumberLabel").text

    def text_if_empty(self):
        return self.driver.find_element_by_css_selector("[class='roboto-bold ng-scope']").text

    def open_menu_user(self):
        self.driver.find_element_by_id("menuUser").click()

    def go_to_my_orders(self):
        self.driver.find_element_by_css_selector("#loginMiniTitle>[class='option ng-scope']").click()

    def fill_SafePay_username_field(self, username):
        self.driver.find_element_by_name("safepay_username").send_keys(username)

    def fill_SafePay_password_field(self, password):
        self.driver.find_element_by_name("safepay_password").send_keys(password)

    def SafePay_pay_now_button(self):
        return self.driver.find_element_by_id("pay_now_btn_SAFEPAY")

    def SafePay_pay_now_button_click(self):
        self.SafePay_pay_now_button().click()

    def order_payment_success(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "orderPaymentSuccess")))
        return self.driver.find_element_by_id("orderPaymentSuccess")

    def thankyou_text(self):
        return self.driver.find_element_by_css_selector('[translate="Thank_you_for_buying_with_Advantage"]').text