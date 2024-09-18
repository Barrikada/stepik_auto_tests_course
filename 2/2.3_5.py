from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()

new_window = browser.window_handles[1]
print(new_window)
browser.switch_to.window(new_window)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

value = browser.find_element(By.ID, "answer")
value.send_keys(y)

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(10)

browser.quit()