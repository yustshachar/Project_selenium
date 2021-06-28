from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\selenium\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.refresh()
driver.maximize_window()






driver.close()
# driver.find_elements_by_css_selector('[data-ng-show="userCookie.response"]')
# driver.find_element_by_id('menuUser').click()
# driver.find_element_by_name('username').send_keys('guy586')
# driver.find_element_by_name('password').send_keys('Ab123456789')
# driver.find_element_by_id("sign_in_btnundefined").click()
# txt = driver.find_element_by_xpath('//nav/ul/li/a/span[@data-ng-show="userCookie.response"][1]').get_attribute('value')
# wait = WebDriverWait(driver, 20)
# wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, '[class="PopUp"]')))
# driver.find_element_by_id('menuUser').click()
# sleep(2)
# txt = driver.find_element_by_css_selector('.containMiniTitle').text
# # print('text:',txt)
# if txt == "":
#     print('txt is empty string',type(txt))
# else:
#     print(type(txt))
# # כניסה לקטגוריית רמקולים
# driver.find_element_by_id("speakersImg").click()
#
# #  בחירת מוצר וכניסה לדף מוצר
# driver.find_element_by_id("21").click()
# name='PURPLE'
# wait = WebDriverWait(self.driver, 20)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id='Layer_1'][version='1.1']")))
# driver.find_element_by_css_selector(f"span[title='{name}'][id='bunny']").click()
# print(driver.find_element_by_css_selector('[class="roboto-regular screen768 ng-binding"]').text)
