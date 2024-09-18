from selenium import webdriver
import os
import time

# Открываем браузер и переходим на страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

# Заполняем текстовые поля
browser.find_element("name", "firstname").send_keys("John")
browser.find_element("name", "lastname").send_keys("Doe")
browser.find_element("name", "email").send_keys("john.doe@example.com")

# Создаем пустой текстовый файл
file_path = "C:/Users/Пользователь/PycharmProjects/Мусор для тестов/file.txt"  # Путь для файла (на Windows можно использовать другой путь)
with open(file_path, "w") as file:
    file.write("")  # Пустой файл

# Загружаем файл
upload_element = browser.find_element("id", "file")
upload_element.send_keys(file_path)

# Нажимаем кнопку "Submit"
browser.find_element("class name", "btn").click()

# Даем время на появление окна с числом
time.sleep(5)

# Закрываем браузер
browser.quit()
