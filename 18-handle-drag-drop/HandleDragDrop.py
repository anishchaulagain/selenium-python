import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://the-internet.herokuapp.com/drag_and_drop'
driver.get(url)

# columns = driver.find_elements(By.ID, value='columns')
#
# for column in columns:
#     print(column.text)

source_element = driver.find_element(By.ID, value="column-a")
destination_element = driver.find_element(By.ID, value="column-b")

actions = ActionChains(driver)

actions.drag_and_drop(source_element, destination_element).perform()
time.sleep(4)

input("enter")