import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

f = open ("product_details.json")

data = json.load(f)

driver = webdriver.Chrome()

driver.get("https://react-shopping-cart-67954.firebaseapp.com/")

items = driver.find_elements(By.CLASS_NAME, "sc-124al1g-2")

for i in items:
    item_name = i.find_element(By.CLASS_NAME, "sc-124al1g-4").text
    item_price = i.find_element(By.CLASS_NAME, "sc-124al1g-6").text

    data["products"].append({
        "name":item_name,
        "price":item_price

    })
time.sleep(10)

def close_system ():
    with open('product_details.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()

while True:
    close_system()
    time.sleep(300)



