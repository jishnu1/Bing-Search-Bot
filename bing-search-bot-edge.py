from selenium import webdriver
import time

driver = webdriver.Edge()

url = "https://www.bing.com/search?q="
ch = 'A'

for i in range(0, 34):
    driver.get(url+ch)
    # time.sleep(1)
    # driver.get(url+ch+ch)
    ch = chr(ord(ch) + 1)
    time.sleep(1)
