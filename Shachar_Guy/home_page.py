class home_page:
    def __init__(self, driver):
        self.driver=driver

    def category(self, name):
        return self.driver.find_element_by_id(f"{name.lower()}Img")

    def click_category(self, name):
        self.category(name).click()

    
