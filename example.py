from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")
def get_author_name():
    author_name = driver.find_element(by="class name", value="author")
    return author_name.text
name = get_author_name()
print(name)
def get_quotes():
    quote = driver.find_element(by="class name", value="col-md-8")
    return quote.text
quote = get_quotes()
print(quote)