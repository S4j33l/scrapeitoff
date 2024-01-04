from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.get("https://chakra-ui.com/docs/styled-system/style-props")
my_table_element_list: WebElement = driver.find_elements(By.TAG_NAME, "tr")
for web_element in my_table_element_list:
    print(web_element.text)
