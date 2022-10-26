from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class MyTest(unittest.TestCase):
    def test_registration1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Name")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Last_name")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("email@email.com")

            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
        

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input_field1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
            input_field2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
            input_field3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")

            input_field1.send_keys("Name")
            input_field2.send_keys("Last_name")
            input_field3.send_keys("email@email.com")

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
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

if __name__ == "__main__":
    unittest.main()