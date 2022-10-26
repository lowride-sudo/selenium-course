from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    driver.get(link)
    time.sleep(5)
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    driver.quit()