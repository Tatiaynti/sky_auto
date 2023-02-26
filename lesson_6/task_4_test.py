from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

firstName = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
firstName.send_keys('Иван')

lastName = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
lastName.send_keys('Петров')

address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
address.send_keys('Ленина, 55-3')

city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
city.send_keys('Москва')

country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
country.send_keys('Россия')

job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
job.send_keys('QA')

company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
company.send_keys('SkyPro')

email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
email.send_keys('test@test.com')

phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
phone.send_keys('79152169609')

driver.find_element(By.CSS_SELECTOR, '#button[type="submit"]').click()

zip = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')

driver.quit()

# tests
def test_empty_zip():
   assert zip == "rgba(15, 81, 50, 1)"

@pytest.mark.parametrize('field, color', 
[(firstName, "rgba(15, 81, 50, 1)"),
(lastName, "rgba(15, 81, 50, 1)"),
(address, "rgba(15, 81, 50, 1)"),
(city, "rgba(15, 81, 50, 1)"),
(country, "rgba(15, 81, 50, 1)"),
(job, "rgba(15, 81, 50, 1)"),
(email, "rgba(15, 81, 50, 1)"),
(phone, "rgba(15, 81, 50, 1)")])

def test_green_fields(field, color):
    assert field == color
