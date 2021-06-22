from unittest import TestCase
from selenium import webdriver
from Shachar_Guy.home_page import home_page
from Shachar_Guy.category_page import category_page
from Shachar_Guy.product_page import product_page

class test_main(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.home_page=home_page(self.driver)
        self.category_page=category_page(self.driver)
        self.product_page=product_page(self.driver)

    def test_1(self):
        self.home_page.click_category("tablets")
        self.category_page.click_product_id(17)
        self.product_page.choose_color("black")


