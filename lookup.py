# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Get Mac Address from command line arguments
address = sys.argv[1]

# Configure Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless

# Start a new instance of the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://www.macvendorlookup.com/")

# search bar input 
search_box = driver.find_element(By.CLASS_NAME, "form-control")

# type the address from the system arguement in the form-control search bar
search_box.send_keys(f"{address}")

# get the result of the search
result = driver.find_element(By.ID, "company")

# convert the text into human readable text
result_text = result.text

# print results
print(result_text)

# let the webpage load for 5 seconds before calling quit()
time.sleep(5)
driver.quit()
