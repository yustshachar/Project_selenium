class product_page:
    def __init__(self, driver):
        self.driver=driver

    def color(self, name):
        self.driver.find_element_by_css_selector(f"[title='{name}']")
        return self.driver.find_element_by_css_selector(f"[title='{name}']")

    def choose_color(self, name):
        self.color(name.upper()).click()

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
        for i in range(1, count):
            self.driver.find_element_by_class_name("plus").click()

    def icon_x_cart(self):
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")

    def icon_x_cart_click(self):
        self.icon_x_cart()[-1].click()

    def card(self):
        return self.driver.find_element_by_id("menuCart")

    def card_click(self):
        self.card().click()

    def price_product(self):

        price_str = self.driver.find_element_by_css_selector("#Description>h2[class='roboto-thin screen768 ng-binding']").text[1:]
        return float(price_str.replace(",", ""))




