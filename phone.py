import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Load the phone numbers from an Excel file
df = pd.read_excel('phone.xls')

# Setup the WebDriver
# Set Chrome options
chrome_options = Options()
# chrome_options.add_argument("--start-fullscreen")  # Open browser in full screen mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Function to perform the search
def search_phone_number(phone_number):
    driver.get('https://www.truepeoplesearch.com/')
    
    try:
        # Wait for the page to load and click the phone search option
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'searchTypePhone-d'))).click()
        
        # Find the input field and enter the phone number
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'PhoneNo')))
        input_field.clear()
        input_field.send_keys(phone_number)
        input_field.send_keys(Keys.ENTER)

        # Wait for results to load (you may need to adjust this or add more specific waits)
        time.sleep(500)

    except Exception as e:
        print(f"An error occurred while searching for {phone_number}: {e}")

# Iterate through each phone number in the DataFrame
for index, row in df.iterrows():
    search_phone_number(row['PhoneNumber'])

# Close the driver
driver.quit()
