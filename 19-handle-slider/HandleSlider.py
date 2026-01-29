import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/horizontal_slider"
driver.get(url)

slider_input = driver.find_element(By.TAG_NAME, value="input")

actions = ActionChains(driver)
actions.click_and_hold(slider_input).move_by_offset(50, 50).release().perform()
time.sleep(5)
driver.quit()


input("enter")