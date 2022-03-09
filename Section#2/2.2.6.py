from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    y=calc(x)


    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox1 = browser.find_element(By.ID,"robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.ID,"robotsRule")
    radiobutton1.click()
    button.click()

    time.sleep(20)
    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(20)
    browser.quit()