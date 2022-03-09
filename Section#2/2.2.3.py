from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, 'num1').text
    x2 = browser.find_element(By.ID, 'num2').text
    y = str(int(x1)+int(x2))
    print(y)

    browser.find_element_by_tag_name("select.custom-select").click()
    browser.find_element_by_css_selector("[value='" + y + "']").click()

    button1 = browser.find_element(By.CSS_SELECTOR,"button.btn.btn-default")
    button1.click()

    time.sleep(20)

finally:
    time.sleep(2)
    browser.quit()