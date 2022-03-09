from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR,'button.btn')
    button.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR,'#input_value').text
    print(x)
    y=calc(x)

    answer = browser.find_element(By.CSS_SELECTOR,'#answer')
    answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    time.sleep(20)

finally:
    time.sleep(10)
    browser.quit()