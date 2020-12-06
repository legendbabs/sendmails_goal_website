import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://www.google.com'

browser.get(url)
time.sleep(2)

'''
<name="q" type="text">

<input  type="submit">
'''

name = "q"
search_el = browser.find_element_by_name(name)

search_el.send_keys('Michael Jackson')

# print(search_el)

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
# print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()
