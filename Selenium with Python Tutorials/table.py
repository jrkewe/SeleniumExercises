import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()
browser.execute_script("window.scrollTo(0,700)")
table = browser.find_element(By.ID,"countries")
rows = table.find_elements(By.TAG_NAME,"tr") #Tags for rows is TR

#Number of rows in the table with header
row_count = len(rows)
print(row_count)

#Number of rows without table header
actual_number = row_count - 1

#Finding a value
target_value = "Australia"
found = False
#Iteration through rows
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td") #Tags for cells in row is TD
    #Iteration through cels in the row
    for cell in cells:
        if target_value in cell.text:
            print(f"Found value'{target_value}'")
            found = True
            break
    if found:
        break
if not found:
    print(f"No value found for '{target_value}'")
