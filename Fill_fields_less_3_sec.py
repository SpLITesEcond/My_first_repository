from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"
find_regular_from_formula = str(math.ceil(math.pow(math.pi, math.e) * 10000))
open_browser = webdriver.Chrome()
open_browser.get(link)
find_link_formula = open_browser.find_element_by_partial_link_text(find_regular_from_formula)
find_link_formula.click()
input1 = open_browser.find_element_by_tag_name("[name=\"first_name\"]")
input1.send_keys("Ivan")
input2 = open_browser.find_element_by_tag_name("[name=\"last_name\"]")
input2.send_keys("Petrov")
input3 = open_browser.find_element_by_tag_name("[name=\"firstname\"]")
input3.send_keys("Smolensk")
input4 = open_browser.find_element_by_id("country")
input4.send_keys("Russia")
button = open_browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(15)
open_browser.quit()
