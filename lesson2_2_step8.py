from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 


current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'new.txt'
file_path = os.path.join(current_dir, file_name)

try:
    driver = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    driver.get(link)

    

    driver.find_element(By.CSS_SELECTOR, "[name = 'firstname']").send_keys('Lol')
    driver.find_element(By.CSS_SELECTOR, "[name = 'lastname']").send_keys('ROFL')
    driver.find_element(By.CSS_SELECTOR, "[name = 'email']").send_keys('email')
    
    driver.find_element(By.ID, 'file').send_keys(file_path)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    driver.quit()



