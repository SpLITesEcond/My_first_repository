from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"
open_browser = webdriver.Chrome()
elements = open_browser.find_elements
open_browser.get(link)
input1 = open_browser.find_element_by_tag_name("[name=\"first_name\"]")
input1.send_keys("Ivan")
input2 = open_browser.find_element_by_tag_name("[name=\"last_name\"]")
input2.send_keys("Petrov")
input3 = open_browser.find_element_by_tag_name("[name=\"firstname\"]")
input3.send_keys("Smolensk")
input4 = open_browser.find_element_by_id("country")
input4.send_keys("Russia")
button = open_browser.find_element_by_xpath("//button[text()='Submit']")
button.click()
time.sleep(15)
open_browser.quit()
