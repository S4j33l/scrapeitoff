import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://quotes.toscrape.com/")
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/p/a")))
print(login_button.text)
login_button.click()
main_heading = driver.find_element(By.LINK_TEXT, "Quotes to Scrape")
print(main_heading.text)