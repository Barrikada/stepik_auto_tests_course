import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"

browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

alert = browser.switch_to.alert
alert.accept()
time.sleep(1)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

value = browser.find_element(By.ID, "answer")
value.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(10)

browser.quit()