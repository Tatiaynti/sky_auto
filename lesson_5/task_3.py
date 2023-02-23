from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_locator = '[onclick="addElement()"]'
add_element = driver.find_element(By.CSS_SELECTOR, add_locator)

for x in range(0,5):
    add_element.click()

delete_btns_length = len(driver.find_elements(By.CSS_SELECTOR, ".added-manually"))
print(delete_btns_length)

sleep(5)