class my_orders_page:
    def __init__(self, driver):
        self.driver = driver

    def order_number(self):
        return self.driver.find_elements_by_css_selector("[rowspan='1']>[class='ng-binding']")