import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.flipkart.com/"
driver.get(url)

def scrape_flipkart(search_query, num_pages=1):
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Flipkart search URL
    base_url = "https://www.flipkart.com/search?q=television" + search_query.replace(" ", "+")
    driver.get(base_url)
    time.sleep(3)  # Wait for the page to load

    products = []
    
    for page in range(num_pages):
        print(f"Scraping page {page+1}...")
        
        # Extract product details
        items = driver.find_elements(By.XPATH, "//div[contains(@class, '_1AtVbE')]//a[contains(@class, '_1fQZEK')]")
        
        for item in items:
            try:
                name = item.find_element(By.XPATH, ".//div[contains(@class, '_4rR01T')]").text
                price = item.find_element(By.XPATH, ".//div[contains(@class, '_30jeq3')]").text
                rating = item.find_element(By.XPATH, ".//div[contains(@class, '_3LWZlK')]").text if item.find_elements(By.XPATH, ".//div[contains(@class, '_3LWZlK')]") else 'N/A'
                link = item.get_attribute("href")
                
                products.append({
                    "Name": name,
                    "Price": price,
                    "Rating": rating,
                    "Link": link
                })
            except Exception as e:
                print("Error extracting data for an item:", e)
        
        # Go to the next page
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, '_1LKTO3') and text()='Next']")
            next_button.click()
            time.sleep(3)
        except:
            print("No more pages available.")
            break
    
    driver.quit()
    
    return pd.DataFrame(products)

if __name__ == "__main__":
    search_term = "washing machine"
    df = scrape_flipkart(search_term, num_pages=2)
    df.to_csv("flipkart_products.csv", index=False)
    print("Data saved to flipkart_products.csv")

# df = pd.DataFrame(products)
# df.to_csv("flipkart_products.csv", index=False)
# print(f"Scraped {len(products)} used cars. Data saved to 'flipkart_products.csv'.")