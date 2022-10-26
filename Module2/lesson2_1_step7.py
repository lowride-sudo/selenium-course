import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(url)


x = browser.find_element(By.CSS_SELECTOR, "h2 > img").get_attribute("valuex")
print(type(x))
y = calc(x)


try:
    browser.find_element(By.ID, "answer" ).send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()