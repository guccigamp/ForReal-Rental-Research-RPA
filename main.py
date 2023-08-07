import time
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


with open(file="config.json", mode="r") as f:
    data = json.load(f)


headers = data["headers"]
listing_website = data["listing_website"]
google_form = data["google_form"]

# Scraping the resulted listings

response = requests.get(listing_website,
                        headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
apartment_listing = []
for listing in soup.find_all("li", class_="list-result-item"):
    house = {
        "Address": f"""{listing.address.p.text.strip()}""",
        "Bedrooms": f"""{listing.find("p", class_="copy-row bed-align").find_all("span")[0].text}""",
        "Price": f"""{listing.find("p", class_="copy-row bed-align").find_all("span")[1].text}""",
        "Link": f"https://forrent.com{listing.a['href']}"
    }
    apartment_listing.append(house)

# Filling the google form

driver = webdriver.Chrome()
for listing in apartment_listing:
    driver.get(google_form)

    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.click()
    address.send_keys(listing["Address"])
    
    time.sleep(2)

    bedroom = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    bedroom.click()
    bedroom.send_keys(listing["Bedrooms"])

    time.sleep(2)

    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.click()
    price.send_keys(listing["Price"])
    
    time.sleep(2)

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.click()
    link.send_keys(listing["Link"])

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

