import time
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://quotes.toscrape.com/")


def systemicActions():
    login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/p/a")
    login_button.click()
    time.sleep(2)
    username_text_field = driver.find_element(By.XPATH, '//*[@id="username"]')
    print(username_text_field.is_displayed())
    username_text_field.send_keys("s4j337")
    password_text_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_text_field.send_keys("admin")

systemicActions()
