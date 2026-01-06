import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Creating an object of Options for webdriver
chrome_options = Options()
chrome_options.add_argument("--incognito")

#Opening the webdriver with an added option
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
time.sleep(5)
url = "https://www.google.com"
browser.get(url)

browser.quit()




