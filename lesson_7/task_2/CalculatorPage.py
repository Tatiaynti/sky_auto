from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self,browser):
        self.waiter = WebDriverWait(browser, 46)
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)

    def time(self, time):
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(time)

    def seven(self):
        a = self._driver.find_element(By.XPATH, "//*[text() ='7']").click()

    def plus(self):
        self._driver.find_element(By.XPATH, "//*[text() ='+']").click()

    def eight(self):
        self._driver.find_element(By.XPATH, "//*[text() ='8']").click()

    def equal(self):
        self._driver.find_element(By.XPATH, "//*[text() ='=']").click()

    def show_on_screen(self):
        self.waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

        screen = self._driver.find_element(By.CSS_SELECTOR, "div.screen").text
        return screen