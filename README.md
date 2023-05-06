# job-scraper

This project is a Python-based web scraper that extracts job listings from [Indeed.com](https://indeed.com) to accelerate the job application process. The scraper uses Selenium to extract information such as job titles, company names, and salary estimates.

## Technologies Used

- **`selenium`**
- **`ChromeDriver`**
- **`xlsxwriter`**

## How to Use the Project

1. Install the required packages by running the following command in your terminal:
   ```zsh
   pip install -r requirements.txt
   ```
2. In the `main` function, update the `search_url()` function with your desired keywords and location to search. For example, to search for "data analyst" positions in "Australia":
   ```python
   search("data analyst", "Australia")
   ```
3. In the `main` function, update the second argument of the `scrape_pages()` function with the number of pages of search results to scrape. For example, the following code extracts job information for the first 5 pages of search results:
   ```python
   scrape_pages("url", 5)
   ```
   By default, the script extracts job information from the first page only.

## Licence

MIT
