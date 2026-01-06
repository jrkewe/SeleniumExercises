import datetime
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

#Dropdown date picker
#Date
current_date = datetime.datetime.now()

#Datepicker
datepicker = browser.find_element(By.ID,"datepicker2")
datepicker.click()

#Selecting the month
#Month has format - mm/2026
#Date
current_month = current_date.month + 1
#Combine month and year
current_month_year = f"{current_month}/2026"

#Finding an element for month
month = browser.find_element(By.XPATH,"//select[@title='Change the month']")
select = Select(month)
#Passing the value
select.select_by_value(str(current_month_year))

#Selecting the year
#Year has format - month/2006-2036
#Date
current_year = current_date.year - 1
#Combine month and year
current_month_year = f"{current_month}/{current_year}"

#Finding an element for year
year = browser.find_element(By.XPATH,"//select[@title='Change the year']")
select = Select(year)
#Passing the value
select.select_by_value(str(current_month_year))

#Selecting a day
#Day has format - link to click
#Date
current_day = str(current_date.day + 1)

#Finding an element for day
browser.find_element(By.LINK_TEXT,current_day).click()








