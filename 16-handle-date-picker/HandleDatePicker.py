from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://leapfrogtechnology.github.io/nepali-date-picker/demo/'
driver.get(url)

driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/fieldset/p/input").click()

# need to be completed

input("enter")