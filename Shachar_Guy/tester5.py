from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

# כניסה לקטגוריית טבלטים
driver.find_element_by_id("tabletsImg").click()
# כניסה לעמוד מוצר
driver.find_element_by_id("18").click()
# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()

driver.find_element_by_css_selector("a[class='ng-binding']").click()

print(len(driver.find_elements_by_css_selector(".categoryDataFixedNav>a")))