from selenium import webdriver
from CalculatorPage import Calculator

def test_fifteen():
    browser = webdriver.Chrome()
    
    calculator = Calculator(browser)
    calculator.time(45)
    calculator.seven()
    calculator.plus()
    calculator.eight()
    calculator.equal()

    screen = calculator.show_on_screen()

    assert screen =='15'