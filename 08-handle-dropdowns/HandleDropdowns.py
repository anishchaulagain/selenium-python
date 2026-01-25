import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
login_url = "http://the-internet.herokuapp.com/dropdown"
driver.get(login_url)
driver.maximize_window()

dropdown_element = driver.find_element(By.ID, value="dropdown")
dropdown_element.click()
time.sleep(1)
select = Select(dropdown_element)

# select the value by visible text
# select the value by index
# select the option by using a value

select.select_by_visible_text("Option 2")
time.sleep(1)
select.select_by_index(1)
time.sleep(1)
select.select_by_value("2")

# count total number of dropdown elements
option_count = len(select.options)
expected_count = 5

if option_count == expected_count:
    print("option count is equal to expected count")

else:
    print("Not as expected")

expected_option = "Option 2"

for option in select.options:
    print(option.text)
    if option.text == expected_option:
        # option.click()
        # print(f"Selected option is {expected_option}")
        print("Found")
    else:
        print("Not found")


input("Enter")


# Take away:
# How to interact with Dropdown
# How to use select class
# How to use 3 different methods
# Select by visible text
# Select by value
# Select by index
# How to count the dropdown values
# Loop the dropdown values and if the desired value found select that value