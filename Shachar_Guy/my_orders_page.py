class my_orders_page:
    def __init__(self, driver):
        self.driver = driver

    def order_number(self):
        return self.driver.find_element_by_css_selector("#myAccountContainer > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > label").text