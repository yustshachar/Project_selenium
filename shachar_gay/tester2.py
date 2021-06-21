from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\yusts\Desktop\שחר\בדיקות תוכנה\sel\chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()



