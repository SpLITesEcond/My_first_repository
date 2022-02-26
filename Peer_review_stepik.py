from selenium import webdriver
import time


#Я так и не понял, дожен ли тест проверять обе сслыки или одну
#Чтобы проверить тест на падение изменить значение↓ на 2
link_1 =  "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link_1)

email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
email.send_keys("Roman@step.ty")
first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
first_name.send_keys("Roman")
last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
last_name.send_keys("Romanyan")
# Отправляем заполненную форму
time.sleep(4)
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы


# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

assert "Congratulations! You have successfully registered!" == welcome_text
time.sleep(8)

browser.quit()
