from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR,'input.form-control[name="firstname"]')
    input1.send_keys("AAA")
    input2 = browser.find_element(By.CSS_SELECTOR,'input.form-control[name="lastname"]')
    input2.send_keys("AAA")
    input3 = browser.find_element(By.CSS_SELECTOR,'input.form-control[name="email"]')
    input3.send_keys("AAA")
    file = browser.find_element(By.CSS_SELECTOR,'input[type="file"]')
    file.send_keys(r'C:\test.txt')
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    time.sleep(20)

finally:
    time.sleep(10)
    browser.quit()