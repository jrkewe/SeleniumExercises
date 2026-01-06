from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/horizontal_slider"
browser.get(url)

#Slider
slider = browser.find_element(By.XPATH,"//input[@type='range']")
actions = ActionChains(browser)

#Moving slider to the right from center
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()
value = slider.get_attribute("value")
print (value)

#Moving slider to the left from center
actions.click_and_hold(slider).move_by_offset(-50,0).release().perform()
print (value)
