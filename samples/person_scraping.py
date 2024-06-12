import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from linkedin_scraper import actions

def scrape_person():
    # Initialize WebDriver
    driver = webdriver.Chrome("C:/Users/ACER/Downloads/chromedriver.exe")

    # LinkedIn login
    email = "rrm07msd@gmail.com"
    password = "RRM@12345"
    actions.login(driver, email, password)  # Login to LinkedIn
    time.sleep(30)
    input("Press Enter")

    # Prompt user to input LinkedIn profile URL
    linkedin_url = input("Enter the LinkedIn profile URL: ")

    # Navigate to the LinkedIn profile URL
    driver.get(linkedin_url)

    # Wait for the profile to load
    time.sleep(10)  # Adjust this wait time as needed

    # Scrape name
    name_element = driver.find_element(By.XPATH, "//*[@class='mt2 relative']")
    name = name_element.find_element(By.TAG_NAME, "h1").text

    # Scrape headline
    try:
        headline_element = driver.find_element(By.CLASS_NAME, "text-body-medium.break-words")
        headline = headline_element.text.strip()
    except NoSuchElementException:
        headline = "Headline not available"

    # Scrape location
    location = name_element.find_element(By.XPATH, "//*[@class='text-body-small inline t-black--light break-words']").text

    # Scrape number of connections
    try:
        connections = driver.find_element(By.CLASS_NAME, "t-bold").text
    except NoSuchElementException:
        connections = "Number of connections not available"

    # Scrape about section
    try:
        about =driver.find_element(By.ID,"about").find_element(By.XPATH,"..").find_element(By.CLASS_NAME,"display-flex").text
    except NoSuchElementException :
        about=None

    
    # Print the scraped information
    print("Name:", name)
    print("Headline:", headline)
    print("Location:", location)
    print("Number of Connections:", connections)
    print("About:", about)
    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    # Call the function to scrape the LinkedIn profile
    scrape_person()
