import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/broken_images"
driver.get(url)

driver.maximize_window()
broken_images = []
image_items = driver.find_elements(By.TAG_NAME, value="img")

for items in image_items:
    src = items.get_attribute("src")
    print(f"images are: {src}")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)

if broken_images:
    for images in broken_images:
        print(f"Broken images are: {images}")

input("enter")