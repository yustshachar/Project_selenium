class category_page:
    def __init__(self, driver):
        self.driver=driver

    def product_id(self, id):
        return self.driver.find_element_by_id(f"{id}")

    def click_product_id(self, id):
        self.product_id(id).click()

    def text_title_page(self):
        return self.driver.find_element_by_class_name("categoryTitle").text