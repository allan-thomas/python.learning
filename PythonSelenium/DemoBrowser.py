
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("Starting Driver")

service_obj = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

val=[]

driver.get("https://rahulshettyacademy.com/")

val.append(driver.title)

driver.get("https://www.google.com/")

val.append(driver.title)

print(val)

driver.maximize_window()

print(driver.current_url)


try:
    assert driver.current_url == "https://www.google.com/i","oh NO"

except AssertionError:
    print("URL is not correct")

driver.close()