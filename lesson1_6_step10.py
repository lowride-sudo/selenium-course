from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_field1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input_field2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input_field3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    
    input_field1.send_keys("Name")
    input_field2.send_keys("Last_name")
    input_field3.send_keys("email@email.com")
    

    # Создание 2х массивов для последующего перебора
    # input_fields = browser.find_elements(By.CSS_SELECTOR, ".first_block input")
    # credentials = ["Name", "Last_name", "email@email.com"]

    # Цикл, который перебирает ссылки в массиве
    # for i in range(3):
    #     input_fields[i].send_keys(credentials[i])

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