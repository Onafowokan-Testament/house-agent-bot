from selenium import webdriver
import time
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
s = Service(chrome_driver_Path)
driver = webdriver.Chrome(service=s)
driver.maximize_window()
form_url ="https://docs.google.com/forms/d/e/1FAIpQLSei7BsZG-eGzCqdUg3b10CeSF93xcaDJS4Kz95zkWQ5EwKZFg/viewform?usp=sf_link"
zillow_url = "https://www.privateproperty.com.ng/houses-for-sale?search=Nigeria&bedroom=&min_price=&max_price=&button="

driver.get(zillow_url)
time.sleep(3)
links = driver.find_elements(By.CSS_SELECTOR, '.similar-listings-info a')
links_href = [value.get_attribute('href') for value in links]
print(links_href)

money = driver.find_elements(By.CSS_SELECTOR, ".similar-listings-price h2 ")
price =[value.text for value in money]
print(price)

addresses = driver.find_elements(By.CLASS_NAME, "listings-location")
location = [value.text for value in addresses]
print(location)

for i in range (len(links_href)):
    driver.get(form_url)
    time.sleep(3)
    property_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(location[i])

    month_price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input ')
    month_price.send_keys(price[i])

    property_link =driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(links_href)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
    print(f"done{i}")