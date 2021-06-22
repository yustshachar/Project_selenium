from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

# כניסה לקטגוריית טבלטים
driver.find_element_by_id("tabletsImg").click()

# כניסה לעמוד מוצר
driver.find_element_by_id("17").click()

# בחירת צבע שחור
driver.find_element_by_css_selector("[title='BLACK']").click()

# הוספת כמות שיהיה 3
driver.find_element_by_name("quantity").click()
driver.find_element_by_name("quantity").clear()
driver.find_element_by_name("quantity").send_keys("3")
sleep(3)

# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()

# חזרה לעמוד הראשי
driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']").click()

# בחירה של קטגוריה לפטופים
driver.find_element_by_id("laptopsImg").click()

# כניסה לעמוד מוצר נוסף
driver.find_element_by_id("2").click()

# בחירת צבע אדום
driver.find_element_by_css_selector("#bunny.RED").click()

# הוספת כמות ל2
driver.find_element_by_name("quantity").clear()
driver.find_element_by_name("quantity").send_keys("5")
sleep(3)

# לחיצה על הוספה לעגלה
driver.find_element_by_name("save_to_cart").click()

# הכנסת הכמות למשתנה
count=driver.find_element_by_css_selector("#shoppingCartLink>span").text
print(count)

if count == 5:
    print("test pass")
else:
    print("test failed")

# חזרה לעמוד הראשי
driver.find_element_by_css_selector("[id='Layer_1'][version='1.1']")

sleep(1)
driver.close()
