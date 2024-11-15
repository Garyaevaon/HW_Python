from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

Username = browser.find_element(
    By.CSS_SELECTOR, "#user-name")
Username.clear()
Username.send_keys("standard_user")

Password = browser.find_element(
    By.CSS_SELECTOR, "#password")
Password.clear()
Password.send_keys("secret_sauce")

button1 = browser.find_element(
    By.CSS_SELECTOR, "#login-button").click()
button2 = browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
button3 = browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
button4 = browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
button5 = browser.find_element(
    By.CSS_SELECTOR, "#shopping_cart_container").click()
button6 = browser.find_element(
    By.CSS_SELECTOR, "#checkout").click()

FirstName = browser.find_element(
    By.CSS_SELECTOR, "#first-name")
FirstName.clear()
FirstName.send_keys("Ольга")

LastName = browser.find_element(
    By.CSS_SELECTOR, "#last-name")
LastName.clear()
LastName.send_keys("Гаряева")

PostalCode = browser.find_element(
    By.CSS_SELECTOR, "#postal-code")
PostalCode.clear()
PostalCode.send_keys("678188")

button = browser.find_element(
    By.CSS_SELECTOR, "#continue").click()

Total = browser.find_element(
    By.CSS_SELECTOR, "div.summary_total_label")
txt = Total.text
print(txt)

browser.quit()

def test_text():
    assert "$58.29" in txt

browser.quit()
