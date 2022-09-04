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
    search_what = driver.find_element(By.XPATH, '//*[@id="text-input-what"]').send_keys(
        what
    )
    search_where = driver.find_element(
        By.XPATH, '//*[@id="text-input-where"]'
    ).send_keys(where)
    submit_search = driver.find_element(By.XPATH, '//*[@id="jobsearch"]/button').click()


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    driver.get(url_indeed)
    search("business analyst", "sydney")


if __name__ == "__main__":
    main()
