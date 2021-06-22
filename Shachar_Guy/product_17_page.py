class product_17_page:
    def __init__(self, driver):
        self.driver=driver

    def color(self, name):
        return self.driver.find_element_by_css_selector(f"[title='{name.upper()}']")

    def choose_color(self, color):
        self.color(color).click()

    def quantity(self):
        return self.driver.find_element_by_name("quantity")

    def choose_quantity(self, num):
        self.quantity().send_keys(f"{num}")