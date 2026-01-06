from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://selenium.dev/")
browser.switch_to.new_window()

browser.get("https://playwright.dev/")

#Counting number of tabs
number_of_tabs=len(browser.window_handles) # Returns: 2
print(number_of_tabs)

#Unique value of tab
tabs_value = browser.window_handles
print(tabs_value) #Returns ['ef2f2d01-0ddf-4881-8aff-7db914a2fab4', 'f8d8888f-2b39-4f06-831a-c1dd184b9b4f'] for two browsers
Current_tab = browser.current_window_handle # Returns currently open tab value: f8d8888f-2b39-4f06-831a-c1dd184b9b4f
print(Current_tab)
#If we want to click on an element on first tab
browser.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()

FirstTab=browser.window_handles[0]
if Current_tab!=FirstTab:
    browser.switch_to.window(FirstTab)
browser.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()