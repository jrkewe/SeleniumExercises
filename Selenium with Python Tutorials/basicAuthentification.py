import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
#Sending login and password directly to the server
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)
time.sleep(5)

elements = browser.find_elements(By.XPATH, "//*[contains(text(), 'Congratulations')]")
assert len(elements) > 0


