from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

waiter = WebDriverWait(driver, 46)

delay = driver.find_element(By.CSS_SELECTOR, "input#delay")
delay.clear()
delay.send_keys("45")
driver.find_element(By.XPATH, '//*[text()="7"]').click()
driver.find_element(By.XPATH, '//*[text()="+"]').click()
driver.find_element(By.XPATH, '//*[text()="8"]').click()
driver.find_element(By.XPATH, '//*[text()="="]').click()

waiter.until(
    expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
)

input_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text

driver.quit()

def test_result():
    assert input_text == "15"