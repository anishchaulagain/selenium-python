import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")


json_data = 'testdata.json'
with open(json_data, 'r') as file:
    json_collection = json.load(file)


for user in json_collection:
    print(user["username"])
    driver.find_element(By.XPATH, value="//input[@id='user-name']").send_keys(user["username"])
    time.sleep(2)
    driver.find_element(By.XPATH, value="//input[@id='password']").send_keys(user["password"])
    time.sleep(2)
    driver.find_element(By.XPATH, value="//input[@id='login-button']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//button[@id='react-burger-menu-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//a[@id='logout_sidebar_link']").click()
