import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/selects2.html"

driver = webdriver.Chrome()
driver.get(url)

try:
    x = int(driver.find_element(By.ID, "num1").text)
    y = int(driver.find_element(By.ID, "num2").text)
    
    
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(x + y))

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(20)
    driver.quit()