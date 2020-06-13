from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:/Users/bumky/Desktop/develop/chromedriver"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")