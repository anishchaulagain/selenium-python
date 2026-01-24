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

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, value="login-button")

assert not login_button.get_attribute("disabled")

login_button.click()

success_element = driver.find_element(By.CSS_SELECTOR, value=".title")

assert success_element.text == "Productss"

input("Enter to quit")