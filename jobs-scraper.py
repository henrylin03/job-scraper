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
    #! should go for elements on page that has all information that we want to scrape - potentially a class
    # search_results = driver.find_elements(By.XPATH, '//*[@id="job_45fce791cd94c471"]')
    search_results = driver.find_elements(By.XPATH, '//*[starts-with(@id, "job_")]')
    for r in search_results:
        print(r.text)

    # '//*[@id="mosaic-provider-jobcards"]/ul/li[7]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/span[1]/a'


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    driver.get(url_indeed)
    search("business analyst", "sydney")
    extract_job_info()


if __name__ == "__main__":
    main()
