from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
el = driver.find_element(By.CSS_SELECTOR, "input.form-control")
el.send_keys("SkyPro")

btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
btn.click()
print(btn.text)

driver.quit()