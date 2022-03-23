from selenium import webdriver
browser = webdriver.Chrome("chromedriver")
browser.get("https://www.morningstar.com/")
input = browser.find_element_by_css_selector(".mdc-search-field__input")
input.send_keys("example text")