from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/nested_frames")

#Top frame
browser.switch_to.frame("frame-top")
#Go to middle frame
browser.switch_to.frame("frame-middle")
#Veryfication
content_middle = browser.find_element(By.ID,"content").text
print("Content in middle frame: ", content_middle)

#Getting to main frame
browser.switch_to.default_content()

#Go to bottom frame
browser.switch_to.frame("frame-bottom")
#Verification
content_bottom = browser.find_element(By.TAG_NAME,"body").text
print("Content in bottom frame: ", content_bottom)