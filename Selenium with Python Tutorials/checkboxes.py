from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
time.sleep(3)

for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)

checked_count = 0
expected_check_count = 3
for checkbox in checkboxes:
    if checkbox.get_attribute("checked"):
        checked_count += 1

if checked_count == expected_check_count:
    print('Check count verified')
else:
    print('Check count mismatch')