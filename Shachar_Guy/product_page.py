class product_page:
    def __init__(self, driver):
        self.driver=driver

    def name(self):
        return self.driver.find_element_by_css_selector('[class="roboto-regular screen768 ng-binding"]')

    def name_text(self):
        name_text = self.name().text
        if len(name_text)>27:
            return name_text[:27]+"..."
        return name_text

    def color(self, name):
        return self.driver.find_element_by_css_selector(f"[class='']>[title='{name}']")

    def choose_color(self, name):
        self.color(name.upper()).click()

    def quantity(self):
        return self.driver.find_element_by_name("quantity")

    def save_to_cart(self):
        return self.driver.find_element_by_name("save_to_cart")

    def save_to_cart_click(self):
        self.save_to_cart().click()

    def back_to_home_page(self):
        return self.driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']")

    def back_to_home_page_click(self):
        self.back_to_home_page().click()

    def choose_quantity(self, count):
        for i in range(1, count):
            self.driver.find_element_by_class_name("plus").click()

    def change_quantity(self, quantity):
        self.driver.find_element_by_css_selector("[name = 'quantity']").click()
        self.driver.find_element_by_css_selector("[name = 'quantity']").send_keys(quantity)

    def icon_x_cart(self):
        return self.driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")

    def icon_x_cart_click(self):
        self.icon_x_cart()[-1].click()

    def cart(self):
        return self.driver.find_element_by_id("menuCart")

    def cart_click(self):
        self.cart().click()

    def price_product(self):
        price_str = self.driver.find_element_by_css_selector("#Description>h2[class='roboto-thin screen768 ng-binding']").text[1:]
        return float(price_str.replace(",", ""))

    def page_bar(self):
        return self.driver.find_elements_by_css_selector("nav>a")

    def checkout_popup(self):
        return self.driver.find_element_by_id("checkOutPopUp")

    def checkout_popup_click(self):
        self.checkout_popup().click()

    def prices_cart_popup(self):
        return self.driver.find_elements_by_css_selector('p[class="price roboto-regular ng-binding"]')

    def prices_cart_popup_text(self):
        prices = self.prices_cart_popup()
        prices_text = []
        for i in prices:
            price = i.text[1:]
            p = float(price.replace(",", ""))
            prices_text.append(p)
        return prices_text

    def names_cart_popup(self):
        return self.driver.find_elements_by_css_selector('h3[class="ng-binding"]')

    def names_cart_popup_text(self):
        names = self.names_cart_popup()
        names_text = []
        for i in names:
            names_text.append(i.text)
        return names_text

    def quantities_cart_popup(self):
        quantities = self.driver.find_elements_by_css_selector("a>label[class='ng-binding']")
        del quantities[1::2]
        return quantities

    def quantities_cart_popup_text(self):
        quantities = self.quantities_cart_popup()
        quantities_text = []
        for i in quantities:
            quantity = i.text[5:]
            quantities_text.append(int(quantity))
        return quantities_text

    def colors_cart_popup(self):
        return self.driver.find_elements_by_css_selector("label>span[class='ng-binding']")

    def colors_cart_popup_text(self):
        colors = self.colors_cart_popup()
        colors_text = []
        for i in colors:
            colors_text.append(i.text)
        return colors_text