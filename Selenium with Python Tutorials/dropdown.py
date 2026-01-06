import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)

#Select the value by visible text
select.select_by_visible_text("Option 2")
time.sleep(5)

#Select the value by Index
select.select_by_index(1)
time.sleep(5)

#Select the option  by using a value
select.select_by_value("2")
time.sleep(5)

#Verify amount of values in dropdown
dropdown_count = len(select.options)
expected_count = 3

if dropdown_count == expected_count:
    print("Test case passed. Count is correct")
else:
    print("Test case failed. Count is incorrect")

#Verify if the value is present in the dropdown
target_value = "Option 2"

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' is not found")