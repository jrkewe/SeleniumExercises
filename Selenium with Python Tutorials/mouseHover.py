import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
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

#Creating ActionChain object
actions = ActionChains(browser)
#Element we want to hover over
hover_element = browser.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
#Move mouse over hover element
actions.move_to_element(hover_element).perform()
#Waiting till mouse will hover over an element
time.sleep(2)
#Clicking on an element that was previously invisible
browser.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()