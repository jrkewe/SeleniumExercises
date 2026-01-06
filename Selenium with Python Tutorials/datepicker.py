import datetime
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/#google_vignette"
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

#Simple date picker
#Closing yellow window
browser.find_element(By.CSS_SELECTOR,"a.close_img").click()

#Moving to iframe with datepicker
iframe = browser.find_element(By.CLASS_NAME,"demo-frame")
browser.switch_to.frame(iframe)

#Datepicker
datepicker = browser.find_element(By.XPATH,"//input[@id='datepicker']")
datepicker.click()

#Example date
current_date = datetime.datetime.now()
next_date = current_date + datetime.timedelta(days=1)
last_date = current_date + datetime.timedelta(days=-1)
#Formating date
formated_date_m_d_Y=current_date.strftime("%m/%d/%Y")
formated_date_d_m_Y=current_date.strftime("%d/%m/%Y")
#Pasing date as text + select date by clicking TAB
datepicker.send_keys(formated_date_d_m_Y + Keys.TAB)