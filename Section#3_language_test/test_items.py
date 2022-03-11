import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)

    browser.implicitly_wait(30)
    button = browser.find_element_by_css_selector("button.btn.btn-add-to-basket")
    assert button != None, "Bucket button is not found!"