from selenium.webdriver.support.select import Select

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


