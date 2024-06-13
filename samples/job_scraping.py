from linkedin_scraper import JobSearch, actions
from selenium import webdriver

# Function to scrape jobs from a LinkedIn job search URL
def scrape_jobs_from_url(url):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome("C:/Users/ACER/Downloads/chromedriver.exe")

    # Email and password for logging in
    email = "youremail@gmail.com"
    password = "yourpassword"

    # Login to LinkedIn
    actions.login(driver, email, password)  # if email and password isn't given, it'll prompt in terminal

    # Create a JobSearch object
    job_search = JobSearch(driver=driver, close_on_complete=False)

    # Navigate to the provided LinkedIn job search URL
    driver.get(url)

    # Perform the job search
    search_term = ""  # No need for search term as we're already on the search results page
    jobs = job_search.search(search_term)

    # Get only the top 10 job listings
    top_10_jobs = jobs[:10]

    # Print the top 10 job listings
    print("Top 10 job listings:")
    for index, job in enumerate(top_10_jobs, start=1):
        print(f"Job {index}:")
        print(f"Title: {job.job_title}")
        print(f"Company: {job.company}")
        print(f"Location: {job.location}")
        print(f"LinkedIn URL: {job.linkedin_url}")
        print("-" * 50)

    # Close the webdriver
    driver.quit()

if __name__ == "__main__":
    print("Welcome to the LinkedIn Job Scraper!")

    # Prompt the user to input the LinkedIn job search URL
    linkedin_url = input("Please enter the LinkedIn job search URL: ")

    # Notify the user to press Enter to start scraping
    input("Press Enter to start scraping...")

    # Call the function to scrape jobs from the provided URL
    scrape_jobs_from_url(linkedin_url)

    print("Scraping completed. Thank you for using the LinkedIn Job Scraper!")
