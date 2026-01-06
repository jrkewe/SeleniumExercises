import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)

#JS alert
#browser.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']").click()
browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
browser.switch_to.alert.accept()

#JS Confirm
#Clicking OK
browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
browser.switch_to.alert.accept()
#Clilcking Cancel
browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
browser.switch_to.alert.dismiss()

#JS Prompt
#Sending message
browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
browser.switch_to.alert.send_keys("Hello World")
browser.switch_to.alert.accept()

#Dismiss sending message
browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
browser.switch_to.alert.dismiss()