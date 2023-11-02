from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")



def main():
    user_input = input("What would you like to find pictures about?   ")

    safe_input = input("Safe search options: \n 0 = off \n 1 = moderate \n 2 = strict ")

    if safe_input == 0:
        button = driver.find_element(By.CLASS_NAME, "js-dropdown-button")
        button.click()
        button = driver.find_element(By.CLASS_NAME, "js-dropdown-items")
        button.click()
    else:
        None
    
    if safe_input == 2:
        None    #MISSING    
    else:
        None

    driver.implicitly_wait(1)

    text_box = driver.find_element(By.ID, "searchbox_input")
    text_box.send_keys(user_input) 

    button = driver.find_element(By.CLASS_NAME, "searchbox_searchButton__F5Bwq")
    button.click()

    driver.implicitly_wait(1)

    button1 = driver.find_element(By.CLASS_NAME, "js-zci-link--images")
    button1.click()

main()


