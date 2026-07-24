import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

print("Starting Driver")

service_obj = Service(r"C:\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name$='name']").send_keys("Allan Thomas")

driver.find_element(By.NAME,"email").send_keys("atk@mail")

driver.find_element(By.XPATH,"//div/input[@id='exampleInputPassword1']").send_keys("atk.8888")

# print(driver.find_element(By.XPATH,"//label[contains(text(),'Check me')]").text)

# print(driver.find_element(By.NAME,"email").text)

driver.find_element(By.ID,"exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,".btn").click()

print(driver.find_element(By.CSS_SELECTOR,".alert").text.split("×\n")[1])

message = driver.find_element(By.CSS_SELECTOR,".alert").text.split("×\n")[1]

try:
    assert message in "Success! The Form has been submitted successfully!"

except AssertionError:
    print("Message is not correct")

for i in range(1,3):
    driver.find_element(By.CSS_SELECTOR,f"#inlineRadio{i}").click()

    time.sleep(3)

driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys(driver.find_element(By.XPATH,"(//h4)[2]").text.split(":")[0])

#static dropdown with select

dropdown = Select(driver.find_element(By.TAG_NAME,"select"))

dropdown.select_by_index(0)
time.sleep(3)
dropdown.select_by_visible_text("Female")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR,".btn").click()

driver.quit()