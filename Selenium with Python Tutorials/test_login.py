from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
def test_EP_1_valid_login():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    username = "standard_user"
    password = "secret_sauce"
    login_url = "https://www.saucedemo.com"
    driver.get(login_url)

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, "login-button")
    assert not login_button.get_attribute("disabled")
    login_button.click()

    success_element = driver.find_element(By.CSS_SELECTOR, ".title")
    assert success_element.text == "Products"

    driver.quit()

