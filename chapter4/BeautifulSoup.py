from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "java"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs =soup.find_all('section',class_="jobs")
    for job in jobs:
        job_posts = job.find_all('li')
        job_posts.pop(-1)
    for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        # print(company.string, kind.string, region.string, title.string)
        job_data = {
            'company' : company.string,
            'region' : region.string,
            'position' : title.string            
        }
        results.append(job_data)
for result in results:
    print(result)
    print("////////////////")
# def say_hello(name, age):
#    print(f"Hello {name} you are {age} years old")

# say_hello("Chris", 33)

