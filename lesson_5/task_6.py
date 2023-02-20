from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")

btn_locator = '.modal-footer>p'
btn_element = driver.find_element(By.CSS_SELECTOR, btn_locator)

btn_element.click()

sleep(5)