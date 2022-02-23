from selenium import webdriver
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/registration2.html"
browser.get(link)
try:
    first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    first_name.send_keys("Roman")
    last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    last_name.send_keys("Romanyan")
    email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    email.send_keys("Roman@step.ty")
    # Отправляем заполненную форму
finally:
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
