class login_in_order_payment_page:
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_name("usernameInOrderPayment")

    def password(self):
        return self.driver.find_element_by_name("passwordInOrderPayment")

    def login_button(self):
        return self.driver.find_element_by_id("login_btnundefined")

    def login_button_click(self):
        self.login_button().click()

    def next_button(self):
        return self.driver.find_element_by_id("next_btn")

    def next_button_click(self):
        self.next_button().click()

    def registration_button(self):
        return self.driver.find_element_by_id("registration_btnundefined")

    def registration_button_click(self):
        self.registration_button().click()