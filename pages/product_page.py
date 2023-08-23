import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math

class ProductPage(BasePage):
    def check_password(self):
        self.add_to_busket()
        self.solve_quiz_and_get_code()
        time.sleep(3)
        self.check_book()

    def add_to_busket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click() 
    
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 5).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name_text = book_name.text
        add_book_name = self.browser.find_element(*ProductPageLocators.ADD_BOOK_NAME)
        add_book_name_text = add_book_name.text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_text = book_price.text
        add_book_price = self.browser.find_element(*ProductPageLocators.ADD_BOOK_PRICE)      
        add_book_price_text = add_book_price.text
        assert book_name_text == add_book_name_text, "books has different name"
        assert book_price_text == add_book_price_text, "books has different price"
        
    def cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be" 
        