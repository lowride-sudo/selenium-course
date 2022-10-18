import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(url)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)


try:
    browser.find_element(By.ID, "answer" ).send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(20)
    browser.quit()