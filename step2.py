import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    time.sleep(5)
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(5)
    button.click()
    time.sleep(5)

# закрываем браузер после всех манипуляций
finally:
    browser.quit()