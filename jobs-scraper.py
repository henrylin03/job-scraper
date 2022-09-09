from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


url_indeed = "https://au.indeed.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def search(what, where):
    what_searchbox = driver.find_element(By.XPATH, '//*[@id="text-input-what"]')
    where_searchbox = driver.find_element(By.XPATH, '//*[@id="text-input-where"]')
    ActionChains(driver).send_keys_to_element(
        what_searchbox, what
    ).send_keys_to_element(where_searchbox, where).send_keys(Keys.ENTER).perform()


def extract_job_info():
    jobs = driver.find_elements(
        By.XPATH, '//div[@class="slider_container css-g7s71f eu4oa1w0"]'
    )
    for job in jobs:
        job_title = job.find_element(
            By.XPATH, ".//*[starts-with(@id, 'jobTitle')]"
        ).text
        print(job_title)


# '//*[@id="mosaic-provider-jobcards"]/ul/li[11]/div'
# '//*[@id="mosaic-provider-jobcards"]/ul/li[13]/div'


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    driver.get(url_indeed)
    search("business analyst", "sydney")
    extract_job_info()


if __name__ == "__main__":
    main()
