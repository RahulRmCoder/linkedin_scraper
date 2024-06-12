import os
from dotenv import load_dotenv
from linkedin_scraper import Person, actions, Company
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Load environment variables from .env file
dotenv_path = 'c:/Users/ACER/Documents/Internships/2.Notion Press/Web Scraping/linkedin1/linkedin_scraper/samples/l.env'
load_dotenv(dotenv_path)

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")

# Print debug statements
print(f"Email: {email}")
print(f"Password: {password}")

# Check if email and password were loaded correctly
if not email or not password:
    raise ValueError("Email or password environment variables not found. Please check your l.env file.")

chrome_driver_path = "C:/Users/ACER/Downloads/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Find and fill email field
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)

# Find and fill password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Check if login was successful
if "feed" in driver.current_url:
    print("Logged in successfully")
else:
    print("Login failed")

user_input = []
urls = []
while True:
    user_input = input("Enter a comma-separated list of LinkedIn URLs: ")
    if user_input.lower() == "exit":
        break
    urls = user_input.split(",")
    results = []
    for url in urls:
        print(f'Scraping {url}')
        person = Person(url, driver=driver, close_on_complete=False)
        print("Name:", person.name)
        print("Location:", person.location)
