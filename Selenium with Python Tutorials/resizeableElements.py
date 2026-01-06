from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)

#Cookies window
wait = WebDriverWait(browser, 10)
try:
    accept = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Consent')]")
        )
    )
    accept.click()
except:
    pass

#Resizable element
resizable_element = browser.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_element = browser.find_element(By.ID, "resizable")
initial_size = initial_element.size
print(initial_size)

#Resize element larger
actions = ActionChains(browser)
actions.click_and_hold(resizable_element).move_by_offset(100,100).release().perform()
initial_size = initial_element.size
print(initial_size)

#Resize element smaller
actions = ActionChains(browser)
actions.click_and_hold(resizable_element).move_by_offset(-20,-20).release().perform()
initial_size = initial_element.size
print(initial_size)