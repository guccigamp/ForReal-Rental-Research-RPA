import time
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# beautifulsoup
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}
response = requests.get("https://www.forrent.com/find/TX/metro-Houston/Sugar+Land/price-Less+than+2100",
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

# selenium

driver = webdriver.Chrome()
for listing in apartment_listing:
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScTLvCd3ds8We9iZT8GYB0imYisaU1Q0Rw0AxuQFkSRzePtNA/viewform?usp=sf_link')

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

