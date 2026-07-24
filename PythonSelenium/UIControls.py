import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print("Starting Driver")

service_obj = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() == True
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected() == True
        break


time.sleep(3)