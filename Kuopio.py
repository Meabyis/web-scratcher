from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()

driver.get("https://duckduckgo.com/")

driver.implicitly_wait(1)

text_box = driver.find_element(By.ID, "searchbox_input")
text_box.send_keys('gbwse') 

button = driver.find_element(By.CLASS_NAME, "searchbox_searchButton__F5Bwq")
button.click()

driver.implicitly_wait(1)

button1 = driver.find_element(By.CLASS_NAME, "js-zci-link--images")
button1.click()
