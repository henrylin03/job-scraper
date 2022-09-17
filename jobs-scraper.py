from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import xlsxwriter


def setup_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--start-maximized")
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
    return DRIVER.current_url


def extract_job_info():
    jobs_list = []
    jobs = DRIVER.find_elements(
        By.XPATH, '//*[@class="slider_container css-g7s71f eu4oa1w0"]'
    )
    try:
        WebDriverWait(DRIVER, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="popover-x"]/button'))
        ).click()
        jobs[0].click()
    except TimeoutException:
        pass
    for j in jobs:
        title_link = j.find_element(By.XPATH, ".//*[starts-with(@id, 'jobTitle')]")
        DRIVER.execute_script("arguments[0].click();", title_link)
        poster = j.find_element(By.CLASS_NAME, "companyName").text
        location = j.find_element(By.CLASS_NAME, "companyLocation").text
        try:
            salary_estimate = j.find_element(
                By.XPATH, './/div[@class="metadata salary-snippet-container"]'
            ).text
        except NoSuchElementException:
            salary_estimate = ""
        try:
            jobs_expanded = DRIVER.find_element(
                By.XPATH,
                '//*[@id="viewJobSSRRoot"]',
            )
            ActionChains(DRIVER).move_to_element(jobs_expanded).perform()
            description_element = jobs_expanded.find_element(
                By.XPATH, './/*[@id="jobDescriptionText"]'
            )
        except NoSuchElementException:
            try:
                jobs_expanded = DRIVER.find_element(
                    By.XPATH, '//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[2]'
                )
                ActionChains(DRIVER).move_to_element(jobs_expanded).perform()
                description_element = jobs_expanded.find_element(
                    By.ID, "jobDescriptionText"
                )
            except NoSuchElementException:
                jobs_expanded = DRIVER.find_element(By.ID, "vjs-container")
                ActionChains(DRIVER).move_to_element(jobs_expanded).perform()
                description_element = DRIVER.find_element(
                    By.XPATH, './/*[@class="jobsearch-JobComponent-embeddedBody"]'
                )
        ActionChains(DRIVER).move_to_element(description_element).perform()
        description_element.text
        jobs_dict = {
            "Job Title": title_link.text,
            "Job Poster": poster,
            "Job Location": location,
            "Description": description_element.text,
            "Estimated Pay": salary_estimate,
            "URL": DRIVER.current_url,
        }
        jobs_list.append(jobs_dict)
    return pd.DataFrame(jobs_list)


def scrape_pages(page1_url, page_count=1):
    if page_count == 1:
        df = extract_job_info()
    elif page_count > 1:
        df_list = []
        for i in range(0, (page_count - 1) * 10, 10):
            page_url = page1_url + f"&start={i}"
            DRIVER.get(page_url)
            df_list.append(extract_job_info())
            df = pd.concat(df_list)
    else:
        raise Exception("Please enter a valid integer greater than 0")
    df_cleaned = df.drop_duplicates().apply(
        lambda x: x.str.strip() if x.dtype == "object" else x
    )
    return df_cleaned


def style_and_export_excel(df):
    writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Indeed", startrow=2, index=False)
    workbook = writer.book
    worksheet = writer.sheets["Indeed"]
    # add title
    worksheet.write(
        0,
        0,
        "Indeed Jobs",
        workbook.add_format({"bold": True, "color": "#2e196d", "size": 14}),
    )
    # format header row
    header_format = workbook.add_format(
        {"bold": True, "text_wrap": True, "fg_color": "#4f3589", "font_color": "white"}
    )
    [
        worksheet.write(2, col_num, col_name, header_format)
        for col_num, col_name in enumerate(df.columns.values)
    ]
    # add border to table
    row_idx, col_idx = df.shape
    for r in range(row_idx):
        for c in range(col_idx):
            worksheet.write(
                r + 3, c, df.values[r, c], workbook.add_format({"border": 1})
            )
    # set column width
    for col in df:
        col_length = max(df[col].astype(str).map(len).max(), len(col))
        col_idx = df.columns.get_loc(col)
        worksheet.set_column(col_idx, col_idx, col_length)
    writer.save()


def main():
    DRIVER.get("https://au.indeed.com/")
    search_url = search("senior business analyst remote", "australia")
    df_cleaned = scrape_pages(search_url, 3)
    style_and_export_excel(df_cleaned)


if __name__ == "__main__":
    main()
