from time import sleep
from pytest import console_main
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

username_locator = 'username'
username_element = driver.find_element(By.ID, username_locator)
username_element.send_keys("tomsmith")

password_locator = 'password'
password_element = driver.find_element(By.ID, password_locator)
password_element.send_keys("SuperSecretPassword!")

btn_locator = 'button'
btn_element = driver.find_element(By.TAG_NAME, btn_locator)
btn_element.click()

sleep(5)