import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://demo.automationtesting.in/Resizable.html'
driver.get(url)

resizable_element = driver.find_element(By.XPATH, value="//body/section/div[@class='container']/div[@class='row']/div[contains(@class,'col-xs-8 col-xs-offset-2')]/div[1]")

initial_element_size = driver.find_element(By.XPATH, value="//div[@id='resizable']")
initial_size = initial_element_size.size
print(initial_size)
time.sleep(5)

actions_chains = ActionChains(driver)
actions_chains.click_and_hold(resizable_element).move_by_offset(180, 180).release().perform()
time.sleep(5)
resizable_element = initial_element_size.size
print(resizable_element)