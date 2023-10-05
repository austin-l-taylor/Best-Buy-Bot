from selenium import webdriver
import time

# file in computer to run chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# website for product
# Enter URL for desired product between quotations
driver.get("https://www.bestbuy.com/site/jlab-audio-go-air-true-wireless-in-ear-headphones-black/6396184."
           "p?skuId=6396184")

foundButton = False

# while the item is out of stock wait 3 seconds and refresh the page and try again
while not foundButton:

    addToCartButton = addButton = driver.find_element_by_class_name("add-to-cart-button")

    if("btn-disabled" in addToCartButton.get_attribute("class")):
        time.sleep(15)
        driver.refresh()

    else:
        foundButton = True

# once item is in stock add it to cart
addToCartButton.click()
time.sleep(10)

# go to your cart
goToCartButton = driver.find_element_by_class_name("go-to-cart-button")
goToCartButton.click()
time.sleep(10)

# go to checkout
goToCheckoutButton = driver.find_element_by_class_name("checkout-buttons__checkout")
goToCheckoutButton.click()
time.sleep(10)

# input login information email and password
# Enter email address between first quote and password in second quote
driver.find_element_by_id("fld-e").send_keys("input email")
driver.find_element_by_id("fld-p1").send_keys("input password")

# sign in button
goToSignInButton = driver.find_element_by_class_name("cia-form__controls")
goToSignInButton.click()
time.sleep(10)

# ccv and submit order
# Enter CCV number between quotes
driver.find_element_by_id("credit-card-cvv").send_keys("input ccv#")
time.sleep(10)

goToSubmitOrderButton = driver.find_element_by_class_name("button--place-order-fast-track")
goToSubmitOrderButton.click()
