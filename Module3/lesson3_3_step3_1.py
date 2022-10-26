from unittest import TestCase, main

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        # create a new Chrome session
        self.driver = webdriver.Chrome()

    def fill_form(self, url):
        self.driver.get(url)

        input1 = self.driver.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys('Ivan')
        input2 = self.driver.find_element(By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys('Petrov')
        input3 = self.driver.find_element(By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys('email@ya.ru')
        input4 = self.driver.find_element(By.XPATH, '//input[@placeholder="Input your phone:"]')
        input4.send_keys('')
        input4 = self.driver.find_element(By.XPATH, '//input[@placeholder="Input your address:"]')
        input4.send_keys('')

        submit_btn = self.driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_btn.click()

    def test_success_registration(self):
        url = 'http://suninjuly.github.io/registration1.html'
        self.fill_form(url)
        welcome_text = self.driver.find_element(By.TAG_NAME, 'h1').text

        self.assertEqual(SUCCESSFUL, welcome_text)

    def test_failed_registration(self):
        url = 'http://suninjuly.github.io/registration2.html'
        self.fill_form(url)
        welcome_text = self.driver.find_element(By.TAG_NAME, 'h1').text

        self.assertEqual(SUCCESSFUL, welcome_text)

    def tearDown(self):
        self.driver.quit()


SUCCESSFUL = 'Congratulations! You have successfully registered!'

if __name__ == "__main__":
    main()