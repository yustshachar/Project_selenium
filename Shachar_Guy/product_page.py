class product_page:
    def __init__(self, driver):
        self.driver=driver

    def color(self, name):
        return self.driver.find_element_by_css_selector(f"[title='{name.upper()}']")

    def choose_color(self, color):
        self.color(color).click()

    def quantity(self):
        return self.driver.find_element_by_name("quantity")

    # def choose_quantity1111(self, num):
    #     self.quantity().clear()
    #     self.quantity().send_keys(f"{num}")

    def save_to_card(self):
        return self.driver.find_element_by_name("save_to_cart")

    def save_to_card_click(self):
        self.save_to_card().click()

    def back_to_home_page(self):
        return self.driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']")

    def back_to_home_page_click(self):
        self.back_to_home_page().click()

    def choose_quantity(self, count):
        while self.driver.find_element_by_name("quantity").text < count:
            self.driver.find_element_by_class_name("plus").click()


