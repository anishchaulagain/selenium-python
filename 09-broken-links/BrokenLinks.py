import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.anishchaulagain.com.np/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

all_url = driver.find_elements(By.TAG_NAME, value='a')

valid_links = []
for link in all_url:
    href = link.get_attribute('href')
    if href:
        valid_links.append(href)
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Link: {href}, status code: {response.status_code}")

print(f"Total number of links {len(all_url)}")
for link in valid_links:
    print(link)

input("Enter")