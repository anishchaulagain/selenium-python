from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://cosmocode.io/automation-practice-webtable/'
driver.get(url)

driver.execute_script('window.scrollTo(0, 700)')

table = driver.find_element(By.ID, value="countries")
rows = table.find_elements(By.TAG_NAME, value="tr")

target_value = "Australia"

for row in rows:
    cells = row.find_elements(By.TAG_NAME, value="td")
    for cell in cells:
        # print(cell.text)
        if target_value in cell.text:
            print(f"Target Value {target_value} found")
        else:
            print("Not found")

print(len(rows))

input("Enter something")