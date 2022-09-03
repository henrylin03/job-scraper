from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


search_url = "https://www.seek.com.au/business-analyst-jobs/in-All-Sydney-NSW"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def extract_job_info():
    search_result_jobs = driver.find_element(By.ID, "app")
    # can I use regex on `class`, or just iterate through the index of Xpath for each job posting?

    print(search_result_jobs.text)


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    driver.get(search_url)
    extract_job_info()


if __name__ == "__main__":
    main()
