import requests
from bs4 import BeautifulSoup
import csv
import re
from selenium import webdriver


url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=data%20scientist&location=Melbourne&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&start=0'
# url = 'https://www.linkedin.com/jobs/search?keywords=data%20scientist&location=Melbourne%2C%20Victoria%2C%20Australia&geoId=100992797&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
file = open('linkedin-jobs.csv', 'a')
writer = csv.writer(file)
writer.writerow(['Title', 'Company'])

def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    response = requests.get(str(next_page))
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip()
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip()

    writer.writerow([
        job_title.encode('utf-8'),
        job_company.encode('utf-8')
    ])

    print('Data updated')

    if page_number < 25:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number)
    else:
        file.close()
        print('File closed')

linkedin_scraper(url, 0)
