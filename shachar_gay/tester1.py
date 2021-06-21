from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

# כניסה לקטגוריית טבלטים
driver.find_element_by_id("tabletsImg").click()

# כניסה לעמוד מוצר
driver.find_element_by_id("17").click()

# בחירת צבע שחור
driver.find_element_by_css_selector(".BLACK").click()

# הוספת כמות שיהיה 3
driver.find_element_by_css_selector(".plus").click()
driver.find_element_by_css_selector(".plus").click()

# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()

# חזרה לעמוד הראשי
driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']")


driver.find_element_by_id("laptopsImg")