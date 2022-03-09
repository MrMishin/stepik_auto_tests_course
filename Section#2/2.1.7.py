from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    img_element = browser.find_element(By.CSS_SELECTOR, 'img[valuex]')
    x = img_element.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    checkbox1 = browser.find_element(By.ID,"robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.ID,"robotsRule")
    radiobutton1.click()
    button1 = browser.find_element(By.CSS_SELECTOR,"button.btn.btn-default")
    button1.click()

    time.sleep(20)

finally:
    time.sleep(2)
    browser.quit()