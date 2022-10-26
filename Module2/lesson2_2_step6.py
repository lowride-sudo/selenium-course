from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    driver.get(link)

    x = driver.find_element(By.ID, "input_value").text
    y = calc(x)

    driver.find_element(By.ID, 'answer').send_keys(y)
    
    driver.find_element(By.ID, "robotCheckbox").click()

    checkbox1 = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
    checkbox1.click()

    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    driver.quit()



