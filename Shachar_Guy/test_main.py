from unittest import TestCase
from openpyxl import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Shachar_Guy.home_page import home_page
from Shachar_Guy.category_page import category_page
from Shachar_Guy.product_page import product_page
from Shachar_Guy.cart_page import cart_page
from Shachar_Guy.login_in_order_payment_page import login_in_order_payment_page
from Shachar_Guy.payment_page import payment_page
from Shachar_Guy.my_orders_page import my_orders_page

class test_main(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.link_web = "https://www.advantageonlineshopping.com/#/"
        self.driver.get(self.link_web)
        self.driver.maximize_window()
        self.driver.refresh()
        self.driver.refresh()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.home_page=home_page(self.driver)
        self.category_page=category_page(self.driver)
        self.product_page=product_page(self.driver)
        self.cart_page=cart_page(self.driver)
        self.login_in_order_payment_page=login_in_order_payment_page(self.driver)
        self.payment_page = payment_page(self.driver)
        self.my_orders_page = my_orders_page(self.driver)
        self.wb = load_workbook("ExcelTesting.xlsx")
        self.xl = self.wb.active

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
        self.product_page.save_to_cart_click()
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
        self.product_page.save_to_cart_click()
        # בדיקה האם חיבור הכמות שווה לכמות המופיעה
        # self.assertEqual(count1 + count2, int(self.driver.find_element_by_css_selector("#shoppingCartLink>span").text))
        if count1 + count2 == int(self.driver.find_element_by_css_selector("#shoppingCartLink>span").text):
            self.xl["A6"] = "passed"
        else:
            self.xl["A6"] = "fails"

    def test_2(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = self.xl["C9"].value
        prod1 = self.xl["C10"].value
        color1 = self.xl["C11"].value
        quantity1 = self.xl["C12"].value
        cat2 = self.xl["E9"].value
        prod2 = self.xl["E10"].value
        color2 = self.xl["E11"].value
        quantity2 = self.xl["E12"].value
        cat3 = self.xl["G9"].value
        prod3 = self.xl["G10"].value
        color3 = self.xl["G11"].value
        quantity3 = self.xl["G12"].value

        # מוצר ראשון
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # בחירת צבע
        self.product_page.choose_color(color1)
        # בחירת כמות
        self.product_page.choose_quantity(quantity1)
        # אחסון השם
        name1 = self.product_page.name_text()
        # אחסון מחיר, אחרי הכפלה בכמות
        price1 = round(quantity1 * self.product_page.price_product(),2)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()

        # מוצר שני
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # בחירת צבע
        self.product_page.choose_color(color2)
        # בחירת כמות
        self.product_page.choose_quantity(quantity2)
        # אחסון השם
        name2 = self.product_page.name_text()
        # אחסון מחיר, אחרי הכפלה בכמות
        price2 = round(quantity2 * self.product_page.price_product(), 2)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()

        # מוצר שלישי
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat3)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod3)
        # בחירת צבע
        self.product_page.choose_color(color3)
        # בחירת כמות
        self.product_page.choose_quantity(quantity3)
        # אחסון השם
        name3 = self.product_page.name_text()
        # אחסון מחיר, אחרי הכפלה בכמות
        price3 = round(quantity3 * self.product_page.price_product(), 2)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # בודק בהתאמה בחלונית עגלת הקניות את השם, צבע, כמות ומחיר של המוצרים שהתווספו
        # שם
        self.assertEqual([name3,name2,name1],self.product_page.names_cart_popup_text())
        # צבע
        self.assertEqual([color3.upper(),color2.upper(),color1.upper()],self.product_page.colors_cart_popup_text())
        # כמות
        self.assertEqual([quantity3,quantity2,quantity1],self.product_page.quantities_cart_popup_text())
        #מחיר
        self.assertEqual([price3,price2,price1],self.product_page.prices_cart_popup_text())

    def test_3(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = self.xl["C16"].value
        prod1 = self.xl["C17"].value
        cat2 = self.xl["E16"].value
        prod2 = self.xl["E17"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()
        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()
        # בודק את כמות המוצרים בעגלה
        before = len(self.product_page.icon_x_cart())
        # מוחק את המוצר האחרון שהצטרף לעגלת קניות
        self.product_page.icon_x_cart_click()
        # בודק שוב את כמות הפריטים בעגלה
        after = len(self.product_page.icon_x_cart())
        # בודק שהכמות ירדה ב1
        # self.assertEqual(before, after+1)
        if before == after+1:
            self.xl["A18"] = "passed"
        else:
            self.xl["A18"] = "fails"

    def test_4(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat3 = "headphones"
        prod3 = "14"
        color3 = "TURQUOISE"
        quantity3 = 6

        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat3)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod3)
        # בחירת צבע
        self.product_page.choose_color(color3)
        # בחירת כמות
        self.product_page.choose_quantity(quantity3)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # מעבר לעמוד עגלת הקניות
        self.product_page.cart_click()

        # בדיקת הופעת הטקסט Shopping Cart למעלה משמאל
        self.assertIn("SHOPPING CART",self.cart_page.nav_current_location().text)

    def test_5(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = self.xl["C26"].value
        prod1 = self.xl["C27"].value
        count1 = self.xl["C28"].value
        cat2 = self.xl["E26"].value
        prod2 = self.xl["E27"].value
        count2 = self.xl["E28"].value
        cat3 = self.xl["G26"].value
        prod3 = self.xl["G27"].value
        count3 = self.xl["G28"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # הכנסת מחיר המוצר כפול הכמות למשתנה
        price_p1 = self.product_page.price_product() * count1
        # בחירת כמות
        self.product_page.choose_quantity(count1)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()
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
        self.product_page.save_to_cart_click()
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
        self.product_page.save_to_cart_click()
        # מעבר לעמוד עגלת הקניות
        self.product_page.cart_click()
        # בדיקה אם המחיר הסופי שווה למחירי המוצרים כפול הכמויות (עם עיגול של 2 ספרות אחרי הנקודה)
        # self.assertEqual(self.cart_page.total(), round(price_p1+price_p2+price_p3,2))
        if self.cart_page.total() == round(price_p1+price_p2+price_p3,2):
            self.xl["A29"] = "passed"
        else:
            self.xl["A29"] = "fails"

        # הדפסת עגלת הקניות
        for i in range(3):
            print(self.cart_page.name_products()[i].text, end="\t")
            print(self.cart_page.quantity_products()[i].text, end="\t")
            print(self.cart_page.price_products()[i].text, end="\t")
            print()

    def test_6(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        cat1 = "speakers"
        prod1 = "20"
        color1 = "GRAY"
        quantity1 = 5
        cat2 = "tablets"
        prod2 = "17"
        color2 = "BLACK"
        quantity2 = 8

        # מוצר ראשון
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat1)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod1)
        # בחירת צבע
        self.product_page.choose_color(color1)
        # בחירת כמות
        self.product_page.choose_quantity(quantity1)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # חזרה לעמוד הראשי
        self.product_page.back_to_home_page_click()

        # מוצר שני
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat2)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod2)
        # בחירת צבע
        self.product_page.choose_color(color2)
        # בחירת כמות
        self.product_page.choose_quantity(quantity2)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()

        # מעבר לעמוד עגלת הקניות
        self.product_page.cart_click()

        # מוצר 2 - הראשון בטבלת עגלת הקניות
        # לחיצה על edit מוצר 2
        self.cart_page.edit_products()[0].click()
        # הורדת הכמות ב2
        self.product_page.minus_quantity(2)
        # שמירה בעגלה ומעבר לעמוד עגלת הקניות
        self.product_page.save_to_cart_click()

        # בדיקת הכמות החדשה - מוצר 2
        self.assertEqual(str(quantity2-2),self.cart_page.quantity_products()[0].text)

        # מוצר 1 - השני בטבלת עגלת הקניות
        # לחיצה על edit מוצר 1
        self.cart_page.edit_products()[1].click()
        # הורדת הכמות ב2
        self.product_page.minus_quantity(2)
        # שמירה בעגלה ומעבר לעמוד עגלת הקניות
        self.product_page.save_to_cart_click()

        # בדיקת הכמות החדשה - מוצר 1
        self.assertEqual(str(quantity1 - 2), self.cart_page.quantity_products()[1].text)

    def test_7(self):
        cat = self.xl["C39"].value
        prod = self.xl["C40"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()
        # חזרה לעמוד הקודם
        self.driver.back()
        # בודק אם הכותרת היא טאבלט
        self.assertEqual(self.category_page.text_title_page(), "TABLETS")
        # חזרה לעמוד הקודם
        self.driver.back()
        # בודק שהכתובת הנוכחית שווה להכתובת של עמוד הבית
        # self.assertEqual(self.driver.current_url, self.link_web)
        if self.driver.current_url == self.link_web:
            self.xl["A41"] = "passed"
        else:
            self.xl["A41"] = "fails"

    def test_8(self):
        pass

    def test_9(self):
        username = self.xl["E50"].value # חייבים משתמש שעוד לא הכניס פרטי אשראי!
        password = self.xl["E51"].value
        # למשתנים ייכנסו הנתונים מהאקסל
        cat = self.xl["C50"].value
        prod = self.xl["C51"].value
        card_num = self.xl["G50"].value
        cvv = self.xl["G51"].value  # באג! הוא מתעלם מהתו הראשון ששמים גם ידנית
        month = self.xl["G52"].value
        year = self.xl["G53"].value
        card_name = self.xl["G54"].value
        # לחיצה לכניסה לעמוד הקטגוריה
        self.home_page.click_category(cat)
        # לחיצה לכניסה לעמוד המוצר
        self.category_page.click_product_id(prod)
        # הכנסה לעגלה
        self.product_page.save_to_cart_click()
        # מעבר לעמוד צ'קאאוט
        self.product_page.checkout_popup_click()
        # הכנסת שם משתמש קיים
        self.login_in_order_payment_page.username().send_keys(username)
        # הכנסת סיסמא קיימת
        self.login_in_order_payment_page.password().send_keys(password)
        # לחיצה על התחברות
        self.login_in_order_payment_page.login_button_click()
        # לחיצה על הבא
        self.login_in_order_payment_page.next_button_click()
        # בחירת תשלום בכרטיס אשראי
        self.payment_page.choose_credit_card()
        # הכנסת פרטי אשראי מהמשתנים
        self.payment_page.card_number().send_keys(card_num)
        self.payment_page.cvv().send_keys(cvv)
        self.payment_page.choose_mm(month)
        self.payment_page.choose_yyyy(year)
        self.payment_page.cardholder_name().send_keys(card_name)
        # לחיצה על כפתור התשלום
        self.payment_page.pay_now_button_click()
        # במידה ופרטי האשראי כבר שמורים למשתמש
        # self.driver.find_element_by_id("pay_now_btn_MasterCredit").click()
        # המתנה לעמוד והכנסת מספר הזמנה למשתנה
        self.wait.until(EC.visibility_of_element_located((By.ID, "orderNumberLabel")))
        order_number = self.payment_page.order_number()
        # מעבר אל עמוד עגלת הקניות
        self.product_page.cart_click()
        # המתנה לעמוד ובדיקה האם המילה empty קיימת שם
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='roboto-bold ng-scope']")))
        self.assertIn("empty", self.payment_page.text_if_empty())
        # לחיצה על user
        self.payment_page.open_menu_user()
        # המתנה שחלונית cart תיעלם ולחיצה על my orders
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "emptyCart")))
        self.payment_page.go_to_my_orders()
        # הכנסת מספר ההזמנה המופיע למשתנה
        num = self.my_orders_page.order_number()
        # בדיקה שאכן מספר ההזמנה שקיבלתי בסיום ההזמנה ומספר ההזמנה שכן שווים
        # self.assertEqual(num, order_number)
        if num == order_number:
            self.xl["A53"] = "passed"
        else:
            self.xl["A53"] = "fails"

    def test_10(self):
        # למשתנים ייכנסו הנתונים מהאקסל
        username = "guy586"
        password = "Ab123456789"

        # התחברות
        # לחיצה על אייקון הuser מצד ימין למעלה באתר
        self.home_page.nav_userIcon_click()
        # מילוי שדה username
        self.home_page.fill_username_field(username)
        # מילוי שדה password
        self.home_page.fill_password_field(password)
        # לחיצה על כפתור SIGN IN
        self.home_page.click_signIn_button()
        # בדיקה שהחיבור הצליח
        self.assertEqual(username,self.home_page.user_miniTitle_text_login())
        self.assertTrue(self.home_page.user_miniTitle().is_displayed())

        # התנתקות
        # לחיצה על אייקון הuser מצד ימין למעלה באתר
        self.home_page.nav_userIcon_click()
        # לחיצה על כפתור Sign out
        self.home_page.click_signOut_button()
        # בדיקה שההתנתקות הצליחה
        self.assertEqual("",self.home_page.user_miniTitle_text_logout())
        self.assertFalse(self.home_page.user_miniTitle().is_displayed())

    def tearDown(self):
        self.wb.save("ExcelTesting.xlsx")
        self.product_page.back_to_home_page_click()
        self.driver.close()