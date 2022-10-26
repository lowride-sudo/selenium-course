from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def registration(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Last_name")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@email.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    finally:
        browser.quit()


def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    assert registration(link) == "Congratulations! You have successfully registered!"

def test_registration2(): 
    link = "http://suninjuly.github.io/registration2.html"
    assert registration(link) == "Congratulations! You have successfully registered!"
    
if __name__ == "__main__":
    test_registration1()
    test_registration2()