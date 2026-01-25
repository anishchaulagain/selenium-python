from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeh3fcL7LztoaybnS7Zx_o1iVoZmxeXLTDyp1BSiz81Zri4-g/viewform")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = driver.find_elements(By.CSS_SELECTOR, value="label[for='i6'] div[class='bzfPab wFGF8']").click()
time.sleep(4)
#
#
# Remaining for checkboxes due to lack of testing website. Task is to just click on checkboxes, and count total number of checkboxes