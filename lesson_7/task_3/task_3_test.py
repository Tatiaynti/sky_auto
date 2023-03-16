from selenium import webdriver
from ShopPage import Authorization, Product, Cart, Buyer, Cost

def test_sum():
    browser = webdriver.Chrome()
    authorization = Authorization(browser)
    authorization.username('standard_user')
    authorization.password('secret_sauce')
    authorization.login()

    product = Product(browser)
    product.sauce_labs_backpack()
    product.sauce_labs_bolt_t_shirt()
    product.sauce_labs_onesie()
    product.go_to_cart()

    cart = Cart(browser)
    cart.checkout()

    buyer = Buyer(browser)
    buyer.first_name("Tatiana")
    buyer.last_name('Mokhnacheva')
    buyer.postal_code('123456')
    buyer.go_next()

    cost = Cost(browser)
    total = cost.price()

    assert total == 'Total: $58.29' 

    browser.quit()
