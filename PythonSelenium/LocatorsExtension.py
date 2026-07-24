import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

print("Starting Driver")

service_obj = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

credentials = ["atk@mail.com","Atk.1881"]

for credential in credentials:
    i=credentials.index(credential)
    driver.find_element(By.XPATH,f"//form/div[{i+1}]/input").send_keys(credential)

driver.find_element(By.CSS_SELECTOR,"#login").click()

driver.switch_to.alert.accept()

time.sleep(2)