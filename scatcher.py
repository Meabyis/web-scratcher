from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import defaultdict

        

def main():  
    user_input = input("What would you like to find about? ")
    
    user_wants = input("Top links = 0 or images = 1: ")

    # Ensure the user entered a valid number for user_wants
    while True:
        try:
            user_wants == int(0 or 1)
            break
        except ValueError:
            print("Please choose a valid option.")
            return     
    
    # Ensure the user entered a valid number for amount_of_search
    while True:
        try:
            amount_of_search = int(input("How many: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    driver = webdriver.Firefox()
    driver.get("https://duckduckgo.com/")
    
    # Find the search input box by ID and enter the user's input
    text_box = driver.find_element(By.ID, "searchbox_input")
    text_box.send_keys(user_input)
    
    # Find the search button by class name and click it
    button = driver.find_element(By.CLASS_NAME, "searchbox_searchButton__F5Bwq")
    button.click()
    
    # Wait for 1 second
    driver.implicitly_wait(1)
    
    # Check if the user wants to see images
    if user_wants == "1":
        # Find the "Images" button by class name and click it
        button1 = driver.find_element(By.CLASS_NAME, "zcm__link.js-zci-link.js-zci-link--images")
        button1.click()

    links = driver.find_elements(By.TAG_NAME, 'a')

    for link in links:
        result_links = link.get_attribute('href')
        if result_links == "javascript:;":
            continue
        elif result_links.startswith("https://duckduckgo.com/"):
            continue
        else:
            print(result_links)                         
        
if __name__ == "__main__":
    main()
