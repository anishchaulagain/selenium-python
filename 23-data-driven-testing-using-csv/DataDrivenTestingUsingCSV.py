import time

from selenium import webdriver
import csv

from selenium.webdriver.common.by import By

csv_file ='testdata.csv'
test_data = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)
print(test_data)

for data in test_data:
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    print(data)
    time.sleep(3)
    driver.find_element(By.ID, value='user-name').send_keys(data['username'])
    driver.find_element(By.ID, value="password").send_keys(data['password'])
    driver.find_element(By.ID, value="login-button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, value='//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, value='//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)
    driver.quit()
