from selenium import webdriver
import time

viewports = [(1024,768),(768,1024),(375,667),(414,896)]
driver = webdriver.Chrome()
driver.get("https://google.com")

time.sleep(5)

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(5)

finally:
    driver.close()