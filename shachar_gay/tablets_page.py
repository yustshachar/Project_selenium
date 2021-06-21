class tablets_page:
    def __init__(self, driver):
        self.driver=driver

    def product_id(self, id):
        return self.driver.find_element_by_id(id)

    def click_product_id(self, id):
        self.product_id(id).click()