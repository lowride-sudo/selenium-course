from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")


try:
    browser.implicitly_wait(5)
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    print(message.text)
finally:
    time.sleep(10)
    browser.quit()
