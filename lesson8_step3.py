from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import math


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element(By.ID, "num1")
    truenumber1 = number1.text
    print("truenumber1 ", truenumber1)
    number2 = browser.find_element(By.ID, "num2")
    truenumber2 = number2.text
    print("truenumber2 ", truenumber2)
    sumnumber = int(truenumber1)+int(truenumber2)
    print("sumnumber ", sumnumber)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sumnumber))
    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()