import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev")
time.sleep(3)
driver.switch_to.new_window()
driver.get("https://www.anishchaulagain.com.np")
# driver.find_element(By.LINK_TEXT, value='Download CV').click()
driver.find_element(By.XPATH, value='/html/body/div[2]/div/section[1]/div/div[2]/div/div[2]/a[1]').click()
input("enter")