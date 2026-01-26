import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

username = "standard_user"
password = "secret_sauce"
# this is the mock login website
login_url = "https://www.saucedemo.com/"

driver.get(login_url)
driver.maximize_window()

username_field = driver.find_element(By.ID, value="user-name")
password_field = driver.find_element(By.ID, value="password")

time.sleep(3)
username_field.send_keys(username)
time.sleep(3)
password_field.send_keys(password)
time.sleep(3)

login_button = driver.find_element(By.ID, value="login-button")

assert not login_button.get_attribute("disabled")

login_button.click()


success_element = driver.find_element(By.CSS_SELECTOR, value=".title")
time.sleep(3)

assert success_element.text == "Products"

input("Enter to quit")