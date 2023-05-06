# job-scraper

This project is a Python-based web scraper that extracts job listings from [Indeed.com](https://indeed.com) to accelerate the job application process. The scraper uses Selenium to extract information such as job titles, company names, and salary estimates.

## Technologies Used

- **`selenium`**
- **`ChromeDriver`**
- **`xlsxwriter`**

## How to Use the Project

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/job-scraper.git
   ```

2. Install the required packages by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. In the `main` function, update the `search_url()` function with your desired keywords and location to search. For example, to search for "data analyst" positions in "Australia":
   ```python
   search("data analyst", "Australia")
   ```
4. In the `main` function, update the second argument of the `scrape_pages()` function with the number of pages of search results to scrape. For example, the following code extracts job information for the first 5 pages of search results:
   ```python
   scrape_pages("url", 5)
   ```
   By default, the script extracts job information from the first page only.
5. Run the script to install ChromeDriver through `ChromeDriverManager().install()`. The script will then extract job posting information as a `pandas` DataFrame and export it to an Excel workbook (`output.xlsx`).
   ```python
   python jobs-scraper.py
   ```
6. To modify the appearance of the output Excel workbook, feel free to modify the `.add_format()` arguments.

## Conclusion

Through developing this job scraper, I sharpened my skills in web scraping and data extraction. Future features may include extracting job postings from other job posting sites, and extracting additional attributes such as type of work and closing date. If you have any feedback or suggestions, please feel free to raise a [GitHub Issue](https://github.com/henrylin03/job-scraper/issues). Thank you for your support!
