from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# switch to top frame
driver.switch_to.frame("frame-top")

# switch to middle frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, value='content')
print(content.text)

# switch to default frame
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")

lower_items = driver.find_elements(By.TAG_NAME, value="body")
for lower in lower_items:
    print(lower.text)

input("enter")