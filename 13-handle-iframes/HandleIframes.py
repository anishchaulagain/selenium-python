# <html>
#     <Iframe>
#         <html>
#         </html>
#     </Iframe>
# <html>
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, value="mce_0_ifr")
driver.switch_to.frame(iframe)

text_editor = driver.find_element(By.ID, value="tinymce")
text_editor.clear()
text_editor.send_keys("Hello this is Anish working on automation")
time.sleep(10)

driver.switch_to.default_content()
# this is done to come out of the iframe
input("enter")