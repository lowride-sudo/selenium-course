from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first")
    input1.send_keys("q")
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    input2.send_keys("w")
    input3 = browser.find_element(By.CSS_SELECTOR, ".second_block .form-control.first")
    input3.send_keys("e")    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()






# browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
