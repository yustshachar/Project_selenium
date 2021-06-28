from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class cart_page:
    def __init__(self, driver):
        self.driver=driver

    def name_products(self):
        return self.driver.find_elements_by_css_selector("[class='roboto-regular productName ng-binding']")

    def quantity_products(self):
        return self.driver.find_elements_by_css_selector("tbody>tr>td>label[class='ng-binding']") #td.quantityMobile>label.ng-binding גיא: גם אפשרי

    def color_products(self):
        return self.driver.find_elements_by_css_selector(".productColor") #.getAttribute("title")

    def price_products(self):
        return self.driver.find_elements_by_css_selector("td[class='smollCell']>p[class='price roboto-regular ng-binding']")

    def edit_products(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'li>#toolTipCart')))
        return self.driver.find_elements_by_css_selector('[translate="EDIT"]')

    def total(self):
        total_str = self.driver.find_element_by_css_selector("[class='fixedTableEdgeCompatibility']>tfoot>tr>td>[class='roboto-medium ng-binding']").text[1:]
        return float(total_str.replace(",", ""))

    def nav_current_location(self):
        return self.driver.find_element_by_css_selector('nav>a[class="select  ng-binding"]')


