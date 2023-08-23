from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    
class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")   
    BOOK_NAME = (By.XPATH, "//*[contains(@class, 'col-sm-6 product_main')]/h1")
    ADD_BOOK_NAME = (By.XPATH, "//*[contains(@class, 'alertinner')]/strong")
    BOOK_PRICE = (By.XPATH, "//*[contains(@class, 'col-sm-6 product_main')]/p")
    ADD_BOOK_PRICE = (By.XPATH, "//*[contains(@class, 'alertinner')]/p/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")

class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//*[div[@id='content_inner']]/div[2]/p")
    GOODS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//*[contains(@href, 'basket')][@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")