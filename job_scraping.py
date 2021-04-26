from bs4 import BeautifulSoup
import requests
import pandas as pd


def extract(page):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    url = f'https://uk.indeed.com/jobs?q=python&l=london&start={page}'
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, "lxml") # convert to beautifulsoup object
    return soup

def find_job(soup):
    jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for index, job in enumerate(jobs):
        title = job.find('a').text.strip()
        company_name = job.find('span', class_= 'company').text.strip()
        job_description = job.find('div', class_ ='summary').text.strip()
        date = job.find('span',class_='date').text.strip()

        try:
            salary = job.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        try:
            type_of_job = job.find('span',class_='remote').text.strip()
        except:
            type_of_job = ''

        job = {"Title": title,
               "Job_Description": job_description,
               "Company": company_name,
               "Salary": salary,
               "Date_published": date
        }

        job_list.append(job)


job_list = []
for i in range(0,40,10):
    print(f"Getting page, {i}")
    c = extract(0)
    find_job(c)



    df = pd.DataFrame(job_list)
    print(df.head())
    df.to_csv('job.csv')

# read dataframe
file = pd.read_csv("job.csv")
file.head()

