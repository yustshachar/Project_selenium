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

    # def tearDown(self):
    #     self.product_page.back_to_home_page_click()
    #     self.driver.close()

    def test_1(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = "tablets"
        prod1=17
        color1 = "black"
        count1=3
        cat2 = "laptops"
        prod2=2
        color2 = "red"
        count2=2
        # לחיצה לכניבה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # בחירת צבע
        self.product_page.choose_color(color1)
        # בחירת כמות
        self.product_page.choose_quantity(count1)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניבה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # בחירת צבע
        self.product_page.choose_color(color2)
        # בחירת כמות
        self.product_page.choose_quantity(count2)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # בדיקה האם חיבור הכמות שווה לכמות המופיעה
        self.assertEqual(count1+count2, self.driver.find_element_by_css_selector("#shoppingCartLink>span").text)




