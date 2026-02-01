from selenium import webdriver

driver = webdriver.Chrome()


username = 'admin'
password = 'admin'

url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
driver.get(url)

# for basic auth: the pattern is https://admin:admin@domain/path