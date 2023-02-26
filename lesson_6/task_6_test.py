from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  
driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Tatiana')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Mokhnacheva')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('111111')

driver.find_element(By.CSS_SELECTOR, '#continue').click()

sum_price = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
driver.quit()

def test_price():
    assert sum_price == 'Total: $58.29'
