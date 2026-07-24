import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print("Starting Driver")

service_obj = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("http://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")

time.sleep(3)

countries = driver.find_elements(By.CSS_SELECTOR,".ui-menu-item a")

count = len(countries)

print(count)


for i in range(1,len(driver.find_elements(By.CSS_SELECTOR,".ui-menu-item a"))):

    if driver.find_element(By.CSS_SELECTOR,f".ui-menu-item:nth-child({i}) a").text == "India":
        driver.find_element(By.CSS_SELECTOR,f".ui-menu-item:nth-child({i}) a").click()
        break

time.sleep(3)

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

