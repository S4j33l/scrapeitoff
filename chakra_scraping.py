from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("https://chakra-ui.com/docs/styled-system/style-props")
my_table_element_list: WebElement = driver.find_elements(By.TAG_NAME, "tr")

with open("chakra_elements.txt", "w") as chakra_elements_file:
    for web_element in my_table_element_list:
        if not (web_element.text.startswith("Prop")):
            split_text = web_element.text.split(",", 1)
            if len(split_text) > 1:
                chakra_elements_file.write(split_text[1].strip() + "\n")
            else:
                chakra_elements_file.write(split_text[0] + "\n")
