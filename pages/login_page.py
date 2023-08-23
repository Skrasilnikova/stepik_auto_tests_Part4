import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
        
    def register_new_user(self, email, password):
        register_email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email_input.send_keys(email)
        register_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password_input.send_keys(password)
        register_password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_password_confirm_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        