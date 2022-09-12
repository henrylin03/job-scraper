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
    # jobs = DRIVER.find_elements(
    #     By.XPATH, '//div[@class="slider_container css-g7s71f eu4oa1w0"]'
    # )
    jobs = DRIVER.find_elements(By.CLASS_NAME, "job_seen_beacon")
    for j in jobs:
        DRIVER.execute_script("arguments[0].click();", j)
        job_title = j.find_element(By.XPATH, ".//*[starts-with(@id, 'jobTitle')]").text
        job_poster = j.find_element(By.CLASS_NAME, "companyName").text
        location = j.find_element(By.CLASS_NAME, "companyLocation").text
        try:
            # salary_estimate = j.find_element(By.CLASS_NAME, "attribute_snippet").text
            salary_estimate = j.find_element(
                By.XPATH, './/div[@class="metadata salary-snippet-container"]'
            ).text
        except NoSuchElementException:
            salary_estimate = ""
        print(job_title, job_poster, location, salary_estimate, sep=" - ")


'//*[@id="mosaic-provider-jobcards"]/ul/li[8]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[3]/div[1]'


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    DRIVER.get(URL_INDEED)
    search("business analyst remote", "australia")
    extract_job_info()


if __name__ == "__main__":
    main()
