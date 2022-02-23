from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[class="first_block"] [class="form-control first"]')
    button.send_keys("Мой отetвет")
    button = browser.find_element(By.CSS_SELECTOR, '[class="first_block"] [class="form-control second"]')
    button.send_keys("Мой отвrtет")
    button = browser.find_element(By.CSS_SELECTOR, '[class="first_block"] [class="form-control third"]')
    button.send_keys("Мой отве т")
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()