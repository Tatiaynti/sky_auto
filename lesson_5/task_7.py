from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

input_locator = 'input'
input_element = driver.find_element(By.TAG_NAME, input_locator)

input_element.send_keys("1000", Keys.RETURN)
input_element.clear()
input_element.send_keys("SkyPro", Keys.RETURN)

sleep(5)