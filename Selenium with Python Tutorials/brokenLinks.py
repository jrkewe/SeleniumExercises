import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://jqueryui.com/"

driver = webdriver.Chrome()
driver.get(url)

links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links: {len(links)}")

broken_links = 0
ok_links = 0
skipped_links = 0

for link in links:
    href = link.get_attribute("href")

    if href is None or href.startswith("#") or not href.startswith("http"):
        skipped_links += 1
        continue

    try:
        response = requests.head(href, allow_redirects=True, timeout=5)
        if response.status_code >= 400:
            print(f" Broken: {href} (status {response.status_code})")
            broken_links += 1
        else:
            ok_links += 1

    except requests.exceptions.RequestException as e:
        print(f" Error: {href} Reason: {e}")
        broken_links += 1

driver.quit()

print(f" OK: {ok_links}, Broken: {broken_links}, Skipped: {skipped_links}")
