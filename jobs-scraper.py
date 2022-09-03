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
    for i in range(1, 23):
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element(
                By.XPATH,
                f'//*[@id="app"]/div/div[4]/div/section/div[2]/div/div[2]/div[1]/div/div/div[2]/div[{i}]/div/article/div[2]/a',
            ),
        )
    # //*[@id="app"]/div/div[4]/div/section/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/article/div[2]/a
    # //*[@id="app"]/div/div[4]/div/section/div[2]/div/div[2]/div[1]/div/div/div[2]/div[22]/div/article/div[2]/a


def main():
    # open given url (later, can have sign-in options, search-bar etc)
    driver.get(search_url)
    extract_job_info()


if __name__ == "__main__":
    main()
