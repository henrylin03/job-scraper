# job-scraper

`job-scraper` searches and extracts job postings from [indeed.com](https://au.indeed.com/) to help with the job application process.

## Description

`job-scraper` is a browser-automation script, written in Python and leveraging the [Selenium](https://selenium-python.readthedocs.io/) framework.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="Python logo" width="150" /> &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="Selenium logo" width="150" />
</p>

Currently, `job-scraper` automates job scraping in Google Chrome.

## How to install

Please install all packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## How to use

1. In `main`, update the `search_url` function with the **key words (_`what=`_), and location (_`where=`_) to search** as strings.

   E.g. to search for "data analyst" positions in "Australia":

```python
search("data analyst", "australia")
```

<p align="center">
  <img src="./img/indeed_search_screenshot.png">
</p>

2. In `main`, update the 2nd argument of the `scrape_pages` function with the **number of pages** to extract job information with a positive integer. By default, the `scrape_pages` function extracts from the first page only.

   E.g. the following will extract information from the first 5 pages of search results:

```python
scrape_pages(search_url, 5)
```

3. Run the script.

## How to contribute

## Credits

## Licence
