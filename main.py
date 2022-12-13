import requests
from bs4 import BeautifulSoup
import time
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=data%20scientist&location=Melbourne&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=0'
# url = 'https://www.linkedin.com/jobs/search?keywords=data%20scientist&location=Melbourne%2C%20Victoria%2C%20Australia&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
# url = "https://au.linkedin.com/jobs/search?keywords=data%20scientist&location=Melbourne%2C%20Victoria%2C%20Australia&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

url = 'https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Melbourne%2C%20Victoria%2C%20Australia&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
# url = 'https://www.linkedin.com/jobs/view/etl-developer-at-barclays-2376164866/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic&originalSubdomain=uk'
# print(url)
# file = open('linkedin-jobs.csv', 'a')
# writer = csv.writer(file)
# writer.writerow(['Title', 'Company'])
urls = [url]

def get_content(url):
    contents = []
    """
    input: an url
    output: skill from webpage
    workflow
     -> resolve response
        -> find element by using xpath
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)

    # pages = url + str(0)
    # response = requests.get(str(pages))
    # reponse = requests.get(str(url+str(0)))
    driver.get(url)
    # doc = BeautifulSoup(response.text, 'html.parser')
    # job = doc.find_all('section', class_='two-pane-serp-page__detail-view')
    # job = doc.find_all('div', class_="details-pane__content")
    # job = driver.find_all('div', class_="base-serp-page__content")
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', attrs={'class':"details-pane__content"})
    # job = driver.find_element(By.ID, '//div[@class="base-serp-page__content"')
    print(table)
    return True
print(get_content(url))



# url = 'https://www.linkedin.com/jobs/view/etl-developer-at-barclays-2376164866/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic&originalSubdomain=uk'
# driver = webdriver.WPEWebKit()
# driver.get(url)
# #Find the job description
# job_desc = driver.find_element_by_xpath('//div[@class="show-more-less-html__markup show-more-less-html__markup--clamp-after-5"]')
# #Get the html of the element and pass into BeautifulSoup parser
# soup = BeautifulSoup(job_desc.get_attribute('outerHTML'), 'html.parser')
# #The parser will print each paragraph on the same line. Use 'separator = \n' to print each each paragraph on a new line and '\n\n' to print an empty line between paragraphs
# soup.get_text(separator='\n\n')


# def get_page_contents(urls):
#   page_contents = []
#   for ind,url in enumerate(urls):
#     response = requests.get(url)
#     time.sleep(2)
#     # use response.status_code to get response status (optional)
#     print("Status code of URL {} is {}".format(ind+1, response.status_code))
#     page_contents.append(response.text)
#   return page_contents
#
# page_contents = get_page_contents(urls)
# print(page_contents)

# def html_pg(page):
#     html = []
#     title = "test-1"
#
#     for i, j in enumerate(page):
#         title = "linkedIn-{}.html".format(i+1)
#         html.append(title)
#         with open(title, 'w', encoding="utf-8") as file:
#             file.write(j)
#     return html
#
# html_files = html_pg(url)
#
# def get_soup(htmls):
#     soups = []
#     for html in htmls:
#         with open(html, 'r') as f:
#           html_source = f.read()
#           doc = BeautifulSoup(html_source, 'html.parser')
#           soups.append(doc)
#           print(type(doc))
#     return soups

# all_soup = get_soup(html_files)
# all_soup

# def linkedin_scraper(webpage, page_number):
#     next_page = webpage + str(page_number)
#     response = requests.get(str(next_page))
#     print(str(next_page))
#     print(response)
#     # soup = BeautifulSoup(webpage, 'html.parser')
#     # soup = BeautifulSoup(response.content, 'html.parser')
#     # print(soup)
#     # jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
#     # jobs = soup.find_all('div', class_='show-more-less-html__markup')
#     # print(jobs)
#     # for job in jobs:
#     #     job_title = job.find('h3', class_='base-search-card__title').text.strip()
#     #     job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()
#
#     # writer.writerow([
#     #     job_title.encode('utf-8'),
#     #     job_company.encode('utf-8')
#     # ])
#
#     print('Data updated')
#
#     if page_number < 25:
#         page_number = page_number + 25
#         linkedin_scraper(webpage, page_number)
#     else:
#         # file.close()
#         print('File closed')

# linkedin_scraper(url, 0)
