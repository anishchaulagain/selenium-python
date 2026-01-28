import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(url)

alert_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/ul/li[1]/button')
alert_button.click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()
time.sleep(3)

alert_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/ul/li[2]/button')
alert_button.click()

alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.dismiss()
time.sleep(3)

alert_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/ul/li[3]/button')
alert_button.click()
time.sleep(3)

alert = driver.switch_to.alert
alert.send_keys("Hello! I'm Anish")
time.sleep(3)
alert.accept()

input("enter")
