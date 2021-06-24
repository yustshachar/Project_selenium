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