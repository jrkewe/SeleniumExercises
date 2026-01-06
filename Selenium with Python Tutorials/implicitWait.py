import time
from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(10)
browser.maximize_window()
url = "https://www.saucedemo.com/"
browser.get(url)

browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()
browser.find_element(By.ID, "react-burger-menu-btn").click()
browser.find_element(By.ID, "logout_sidebar_link").click()

browser.quit()

