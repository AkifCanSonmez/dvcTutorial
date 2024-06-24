import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.binary_location = '/usr/bin/chromium'
chrome_options.add_argument('--headless')  # Set headless mode to True

# Install ChromeDriver and configure service
service = Service(ChromeDriverManager().install())

# Create a Chrome driver instance with the specified options
driver = webdriver.Chrome(service=service, options=chrome_options)


# Initialize Chrome driver with configured service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google Images and search for "banana"
driver.get("https://images.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("banana")
search_box.send_keys(Keys.RETURN)

# Ensure the dataset directory exists
dataset_path = 'dataset'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Determine the starting index to avoid overwriting existing images
existing_files = [f for f in os.listdir(dataset_path) if f.endswith('.png')]
starting_index = max([int(f.split('_')[1].split('.')[0]) for f in existing_files], default=0) + 1

# Scrape images
for i in range(starting_index, starting_index + 2):  # Change the range as needed
    # Logic to load and save images goes here, including scrolling if necessary
    # For simplicity, here we're just using a placeholder for the actual image saving logic
    screenshot_path = os.path.join(dataset_path, f'image_{i}.png')
    driver.save_screenshot(screenshot_path)  # This would be replaced with actual image saving logic
    print(f'Saved screenshot to {screenshot_path}')
    time.sleep(2)  # Be respectful in your scraping

driver.quit()
