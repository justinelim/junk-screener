"""
Method 1: Scraping with Selenium
"""

from selenium import webdriver

browser = webdriver.Chrome("chromedriver")
browser.get("https://financials.morningstar.com/ratios/r.html?t=arct")
operating_cash_flow = browser.find_elements_by_id("i9")
# input.send_keys("example text")
operating_cash_flow = [t.text for t in operating_cash_flow]
print(operating_cash_flow)