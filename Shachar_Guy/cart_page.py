class cart_page:
    def __init__(self, driver):
        self.driver=driver

    def name_products(self):
        return self.driver.find_elements_by_css_selector("[class='roboto-regular productName ng-binding']")

    def quantity_products(self):
        return self.driver.find_elements_by_css_selector("tbody>tr>td>label[class='ng-binding']")

    def color_products(self):
        return self.driver.find_elements_by_css_selector(".productColor") #.getAttribute("title")

    def price_products(self):
        return self.driver.find_elements_by_css_selector("td[class='smollCell']>p[class='price roboto-regular ng-binding']")

    def total(self):
        total_str = self.driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']>tfoot>tr>td>[class='roboto-medium ng-binding']").text[1:]
        return float(total_str.replace(",", ""))

    def nav_current_location(self):
        return self.driver.find_element_by_css_selector('nav>a[class="select  ng-binding"]')


