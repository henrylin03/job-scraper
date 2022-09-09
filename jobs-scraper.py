from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


URL_INDEED = "https://au.indeed.com/"
DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def search(what, where):
    what_searchbox = DRIVER.find_element(By.XPATH, '//*[@id="text-input-what"]')
    where_searchbox = DRIVER.find_element(By.XPATH, '//*[@id="text-input-where"]')
    ActionChains(DRIVER).send_keys_to_element(
        what_searchbox, what
    ).send_keys_to_element(where_searchbox, where).send_keys(Keys.ENTER).perform()


def extract_job_info():
    job_results = DRIVER.find_elements(By.XPATH, "//*[starts-with(@id, 'jobTitle')]")
    for j in job_results:
        expand_results = DRIVER.execute_script(
            "arguments[0].click();", j
        )  # expands search result
        print(j)

    # for j in jobs:
    #     j.click()
    #     job_title = j.find_element(By.XPATH, ".//*[starts-with(@id, 'jobTitle')]").text
    #     job_poster = j.find_element(By.CLASS_NAME, "companyName").text
    #     location = j.find_element(By.CLASS_NAME, "companyLocation").text
    #     # salary_estimate = j.find_element(
    #     #     By.XPATH, ".//*[starts-with(@id, 'salaryInfoAndJobType')]"
    #     # ).text
    #     print(job_title, job_poster, location, sep=" - ")


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    DRIVER.get(URL_INDEED)
    search("business analyst", "sydney")
    extract_job_info()


if __name__ == "__main__":
    main()
