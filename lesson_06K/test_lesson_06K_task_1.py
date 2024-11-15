import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

FirstName = browser.find_element(
    By.CSS_SELECTOR, 'input[name="first-name"]'
    )
FirstName.clear()
FirstName.send_keys("Иван")

lastName = browser.find_element(
    By.CSS_SELECTOR, 'input[name="last-name"]'
    )
lastName.clear()
lastName.send_keys("Петров")

address = browser.find_element(
    By.CSS_SELECTOR, 'input[name="address"]'
    )
address.clear()
address.send_keys("Ленина, 55-3")

email = browser.find_element(
    By.CSS_SELECTOR, 'input[name="e-mail"]'
    )
email.clear()
email.send_keys("test@skypro.com")

phone = browser.find_element(
    By.CSS_SELECTOR, 'input[name="phone"]'
    )
phone.clear()
phone.send_keys("+7985899998787")

zipcode = browser.find_element(
    By.CSS_SELECTOR, 'input[name="zip-code"]'
    )
zipcode.clear()

city = browser.find_element(
    By.CSS_SELECTOR, 'input[name="city"]'
    )
city.clear()
city.send_keys("Москва")

country = browser.find_element(
    By.CSS_SELECTOR, 'input[name="country"]'
    )
country.clear()
country.send_keys("Россия")

jobposition = browser.find_element(
    By.CSS_SELECTOR, 'input[name="job-position"]'
    )
jobposition.clear()
jobposition.send_keys("QA")

company = browser.find_element(
    By.CSS_SELECTOR, 'input[name="company"]'
    )
company.clear()
company.send_keys("SkyPro")

button = browser.find_element(
    By.CSS_SELECTOR, "button.btn-outline-primary"
    ).click()

def test_FirstName():
    assert "success" in browser.find_element(
    By.ID, "first-name").get_attribute("class")

def test_lastName():
    assert "success" in browser.find_element(
    By.ID, "last-name").get_attribute("class")

def test_3():
    assert "success" in browser.find_element(
    By.ID, "address").get_attribute("class")

def test_4():
    assert "success" in browser.find_element(
    By.ID, "e-mail").get_attribute("class")

def test_5():
    assert "success" in browser.find_element(
    By.ID, "phone").get_attribute("class")

def test_6():
    assert "danger" in browser.find_element(
    By.ID, "zip-code").get_attribute("class")
def test_7():
    assert "success" in browser.find_element(
    By.ID, "city").get_attribute("class")

def test_8():
    assert "success" in browser.find_element(
    By.ID, "country").get_attribute("class")
        
def test_9():
    assert "success" in browser.find_element(
    By.ID, "job-position").get_attribute("class")

def test_10():
    assert "success" in browser.find_element(
    By.ID, "company").get_attribute("class")

browser.quit()
