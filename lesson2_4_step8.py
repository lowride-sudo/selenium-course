
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
try:
    WebDriverWait(driver, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100')
        )
        
    driver.find_element(By.CSS_SELECTOR, '#book').click()

    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, 'input_value')))

    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    driver.find_element(By.ID, "answer" ).send_keys(y)
    driver.find_element(By.CSS_SELECTOR, "#solve").click()


finally:
    time.sleep(20)
    driver.quit()