from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, заполняющий обязательные поля
    firstNameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    firstNameInput.send_keys("test")
    emailInput = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    emailInput.send_keys("test")
    lastNameInput = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    lastNameInput.send_keys("test")
    
    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегестрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание, чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер
    browser.quit()
    