from unittest import TestCase
from openpyxl import *
from selenium import webdriver
from time import sleep
from Shachar_Guy.home_page import home_page
from Shachar_Guy.category_page import category_page
from Shachar_Guy.product_page import product_page
from Shachar_Guy.card_page import card_page

class test_main(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.link_web = "https://www.advantageonlineshopping.com/#/"
        self.driver.get(self.link_web)
        self.driver.maximize_window()
        self.home_page=home_page(self.driver)
        self.category_page=category_page(self.driver)
        self.product_page=product_page(self.driver)
        self.card_page=card_page(self.driver)
        self.xl = load_workbook("ExcelTesting.xlsx").active

    def tearDown(self):
        self.product_page.back_to_home_page_click()
        self.driver.close()

    def test_1(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = self.xl["C2"].value
        prod1 = self.xl["C3"].value
        color1 = self.xl["C4"].value
        count1= self.xl["C5"].value
        cat2 = self.xl["E2"].value
        prod2=self.xl["E3"].value
        color2 = self.xl["E4"].value
        count2= self.xl["E5"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # בחירת צבע
        # self.product_page.choose_color(color1)
        # בחירת כמות
        self.product_page.choose_quantity(count1)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # בחירת צבע
        # self.product_page.choose_color(color2)
        # בחירת כמות
        self.product_page.choose_quantity(count2)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # בדיקה האם חיבור הכמות שווה לכמות המופיעה
        self.assertEqual(count1+count2, int(self.driver.find_element_by_css_selector("#shoppingCartLink>span").text))

    def test_2(self):
        pass

    def test_3(self):
        cat1 = self.xl["C13"].value
        prod1 = self.xl["C14"].value
        cat2 = self.xl["E13"].value
        prod2 = self.xl["E14"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # בודק את כמות המוצרים בעגלה
        before = len(self.product_page.icon_x_cart())
        # מוחק את המוצר האחרון שהצטרף לעגלת קניות
        self.product_page.icon_x_cart_click()
        # בודק שוב את כמות הפריטים בעגלה
        after = len(self.product_page.icon_x_cart())
        # בודק שהכמות ירדה ב1
        self.assertEqual(before, after+1)

    def test_4(self):
        pass

    def test_5(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = self.xl["C22"].value
        prod1 = self.xl["C23"].value
        count1 = self.xl["C24"].value
        cat2 = self.xl["E22"].value
        prod2 = self.xl["E23"].value
        count2 = self.xl["E24"].value
        cat3 = self.xl["G22"].value
        prod3 = self.xl["G23"].value
        count3 = self.xl["G24"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # הכנסת מחיר המוצר כפול הכמות למשתנה
        price_p1 = self.product_page.price_product() * count1
        # בחירת כמות
        self.product_page.choose_quantity(count1)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # הכנסת מחיר המוצר כפול הכמות למשתנה
        price_p2 = self.product_page.price_product() * count2
        # בחירת כמות
        self.product_page.choose_quantity(count2)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat3)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod3)
        # הכנסת מחיר המוצר כפול הכמות למשתנה
        price_p3 = self.product_page.price_product() * count3
        # בחירת כמות
        self.product_page.choose_quantity(count3)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # מעבר לעמוד עגלת הקניות
        self.product_page.card_click()
        # בדיקה אם המחיר הסופי שווה למחירי המוצרים כפול הכמויות (עם עיגול של 2 ספרות אחרי הנקודה)
        self.assertEqual(self.card_page.total(), round(price_p1+price_p2+price_p3,2))
        # הדפסת עגלת הקניות
        for i in range(3):
            print(self.card_page.name_products()[i].text, end="\t")
            print(self.card_page.quantity_products()[i].text, end="\t")
            print(self.card_page.price_products()[i].text, end="\t")
            print()

    def test_6(self):
        pass

    def test_7(self):
        cat = "tablets"
        prod = 18
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod)
        # הכנסה לעגלה
        self.product_page.save_to_card_click()
        # חזרה לעמוד הקודם
        self.driver.back()
        # בודק אם הכותרת היא טאבלט
        self.assertEqual(self.category_page.text_title_page(), "TABLETS")
        # חזרה לעמוד הקודם
        self.driver.back()
        # בודק שהכתובת הנוכחית היא הכתובת של עמוד הבית
        self.assertEqual(self.driver.current_url, self.link_web)

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass














