from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

# כניסה לקטגוריית טבלטים
driver.find_element_by_id("tabletsImg").click()
# כניסה לעמוד מוצר
driver.find_element_by_id("17").click()
# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()
# חזרה לעמוד הראשי
driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']").click()
# בחירה של קטגוריה לפטופים
driver.find_element_by_id("laptopsImg").click()
# כניסה לעמוד מוצר נוסף
driver.find_element_by_id("2").click()
# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()
#מכניס לרשימה את האיקסים
xbuttons = driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")
befor = len(xbuttons)
#לוחץ על האיקס האחרון שהצטרף
xbuttons[-1].click()
after = len(xbuttons)
print(befor)
print(len(driver.find_elements_by_css_selector("[class='removeProduct iconCss iconX']")))


#
# # חזרה לעמוד הראשי
# driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']")
# sleep(2)
# driver.close()
