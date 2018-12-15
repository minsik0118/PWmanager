from selenium import webdriver
import time
username='minsik0118@naver.com'
password='alstlr009953'
url='https://www.facebook.com/'

driver = webdriver.Chrome("C:/Users/minsi/Downloads/chromedriver_win32/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()