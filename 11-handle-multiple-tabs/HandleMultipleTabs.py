import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev")
time.sleep(3)
driver.switch_to.new_window()
driver.get("https://www.anishchaulagain.com.np")
input("enter")