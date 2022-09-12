from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


URL_INDEED = "https://au.indeed.com/"


def setup_chrome_driver():
    options = Options()
    return webdriver.Chrome(
        options=options, service=Service(ChromeDriverManager().install())
    )


DRIVER = setup_chrome_driver()


def search(what, where):
    what_searchbox = DRIVER.find_element(By.XPATH, '//*[@id="text-input-what"]')
    where_searchbox = DRIVER.find_element(By.XPATH, '//*[@id="text-input-where"]')
    ActionChains(DRIVER).send_keys_to_element(
        what_searchbox, what
    ).send_keys_to_element(where_searchbox, where).send_keys(Keys.ENTER).perform()


def extract_job_info():
    jobs = DRIVER.find_elements(
        By.XPATH, '//*[@class="slider_container css-g7s71f eu4oa1w0"]'
    )
    for j in jobs:
        title_link = j.find_element(By.XPATH, ".//*[starts-with(@id, 'jobTitle')]")
        DRIVER.execute_script("arguments[0].click();", title_link)
        title = title_link.text
        poster = j.find_element(By.CLASS_NAME, "companyName").text
        location = j.find_element(By.CLASS_NAME, "companyLocation").text
        try:
            salary_estimate = j.find_element(
                By.XPATH, './/div[@class="metadata salary-snippet-container"]'
            ).text
        except NoSuchElementException:
            salary_estimate = ""
        try:
            jobs_expanded = DRIVER.find_element(By.ID, "vjs-container")
            job_description = jobs_expanded.find_element(
                By.XPATH, './/*[@class="jobsearch-JobComponent-embeddedBody"]'
            ).text
        except NoSuchElementException:
            jobs_expanded = DRIVER.find_element(By.CLASS_NAME, "jobsearch-RightPane")
            job_description = jobs_expanded.find_element(
                By.ID, "jobDescriptionText"
            ).text


def main():
    DRIVER.get(URL_INDEED)
    search(what="business analyst remote", where="australia")
    extract_job_info()


if __name__ == "__main__":
    main()
