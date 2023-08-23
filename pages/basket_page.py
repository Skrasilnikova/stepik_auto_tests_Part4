import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math

class BasketPage(BasePage):
    def check_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket empty message is not presented, but should be"
        empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        empty_text = empty.text
        assert ("Ваша корзина пуста" in empty_text), "Basket empty message is not correct"
        
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), "Goods in basket, but should not be"