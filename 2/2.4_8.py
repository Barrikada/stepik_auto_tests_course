from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

price_button = browser.find_element(By.ID, "book")
price_button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

value = browser.find_element(By.ID, "answer")
value.send_keys(y)

submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

time.sleep(10)

browser.quit()
