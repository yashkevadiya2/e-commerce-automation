from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

def automation():

    usertextfield = driver.find_element(By.ID, "user-name")
    passwordfiled = driver.find_element(By.ID, "password")
    loginbutton = driver.find_element(By.ID,"login-button")

    usertextfield.send_keys("standard_user")
    passwordfiled.send_keys("secret_sauce")
    loginbutton.click()
    time.sleep(5)

    swaglabs = driver.find_elements(By.CLASS_NAME,"inventory_item")
    backpackscart = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
    tshirtscart = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")

    items_to_add = ["Sauce Labs Backpack","Sauce Labs Bike Light"]
    item = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    for e in item:
        if e.find_element(By.CLASS_NAME, "inventory_item_name ").text in items_to_add:
             e.find_element(By.CLASS_NAME, "btn_inventory").click()


    cartitem = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    cartitem.click()
    time.sleep(5)

    checkoutclick = driver.find_element(By.ID, "checkout")
    checkoutclick.click()
    time.sleep(3)

    firstnamefill = driver.find_element(By.ID,"first-name")
    lastnamefill = driver.find_element(By.ID, "last-name")
    pincodefill = driver.find_element(By.ID, "postal-code")

    firstnamefill.send_keys("yashkumar")
    lastnamefill.send_keys("kevadiya")
    pincodefill.send_keys("10713")
    time.sleep(5)

    givecontinue1 = driver.find_element(By.ID, "continue")
    givecontinue1.click()
    time.sleep(5)

    finish1 = driver.find_element(By.ID, "finish")
    finish1.click()
    time.sleep(10)

def add_tocart_byprice():

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()


    items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    for i in items:
        price = i.find_element(By.CLASS_NAME, "inventory_item_price").text
        priceint = float(price[1:])
        if priceint <= 12:
            i.find_element(By.CLASS_NAME,"btn_inventory ").click()
    
    time.sleep(10)

    cartitem = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    cartitem.click()
    time.sleep(5)

def add_tshirt_cart():
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    items = driver.find_elements(By.CLASS_NAME,"inventory_item")

    for j in items:
        item_name = j.find_element(By.CLASS_NAME,"inventory_item_name ").text

        if "backpack" in item_name:
            j.find_element(By.CLASS_NAME, "btn_inventory ").click()

        time.sleep(5)

    cartitem = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
    cartitem.click()
    time.sleep(5)

if __name__ == "__main__":
    add_tshirt_cart()
