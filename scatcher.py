from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")

amount_of_search = int()

def main():
    user_input = input("What would you like to find about?   ")



    user_wants = input("Top links = 0 or images = 1    ")



    amount_of_search = input("How many?   ")

    text_box = driver.find_element(By.ID, "searchbox_input")
    text_box.send_keys(user_input) 

    button = driver.find_element(By.CLASS_NAME, "searchbox_searchButton__F5Bwq")
    button.click()

    driver.implicitly_wait(1)

    button1 = driver.find_element(By.CLASS_NAME, "js-zci-link--images")
    button1.click()

if __name__=="__main__":
    main()


