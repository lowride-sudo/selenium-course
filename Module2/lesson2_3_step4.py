import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = "http://suninjuly.github.io/alert_accept.html"

driver = webdriver.Chrome()
driver.get(url)




try:
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary" ).click()
    confirm = driver.switch_to.alert
    confirm.accept()
    
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, 'input_value')))

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    driver.find_element(By.ID, "answer" ).send_keys(y)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


finally:
    time.sleep(20)
    driver.quit()