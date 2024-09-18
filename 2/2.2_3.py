import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    num_1 = browser.find_element(By.ID, "num1")
    num_2 = browser.find_element(By.ID, "num2")
    num_1 = int(num_1.text)
    num_2 = int(num_2.text)
    result = num_1 + num_2
    value = Select(browser.find_element(By.TAG_NAME, "select"))
    value.select_by_value(str(result))
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(10)
finally:
    browser.quit()
