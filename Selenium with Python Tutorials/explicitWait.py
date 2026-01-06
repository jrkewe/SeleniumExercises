from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))

element.click()

browser.quit()

