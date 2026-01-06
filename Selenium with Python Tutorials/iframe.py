import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

browser = webdriver.Firefox()
browser.get("https://selectorshub.com/iframe-scenario/")
browser.maximize_window()

time.sleep(5)

iframe = browser.find_element(By.ID, "pact1")
browser.switch_to.frame(iframe)

input_field = browser.find_element(By.ID,"inp_val" )
#Clear text editor
input_field.clear()
input_field.send_keys("Hello World")

iframe2 = browser.find_element(By.ID, "pact2")
browser.switch_to.frame(iframe2)

input_field2 = browser.find_element(By.ID,"jex" )
#Clear text editor
input_field2.clear()
input_field2.send_keys("Hello World2")

iframe3 = browser.find_element(By.ID, "pact3")
browser.switch_to.frame(iframe3)

input_field3 = browser.find_element(By.ID,"glaf" )
#Clear text editor
input_field3.clear()
input_field3.send_keys("Hello World3")

browser.switch_to.default_content()
selenium_link = browser.find_element(By.XPATH,"//header//a[@href='https://selectorshub.com']").click()




