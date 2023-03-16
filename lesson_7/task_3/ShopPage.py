from selenium.webdriver.common.by import By

class Authorization:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(15)

    def username(self, username):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)

    def password(self, password):
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

class Product:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(15)

    def sauce_labs_backpack(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    
    def sauce_labs_bolt_t_shirt(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def sauce_labs_onesie(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()

class Cart:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

class Buyer:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def first_name(self, first_name):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def last_name(self, last_name):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def postal_code(self, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

    def go_next(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

class Cost:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def price(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return txt