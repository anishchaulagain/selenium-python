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

input("enter")
