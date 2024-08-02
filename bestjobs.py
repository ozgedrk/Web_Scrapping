import requests
from bs4 import BeautifulSoup

headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
glassdor = requests.get("https://bilative.github.io/sisterslab/web_scraping",headers=headers_param)

# print(glassdor.content)
# print(glassdor.status_code)

jobs = glassdor.content
 
soup = BeautifulSoup(jobs,"html.parser")

# print(soup.title)
# print(soup.find("h3").text)

# print(soup.find_all("div"))

# print(soup.find_all("a"))

all_jobs = soup.find_all("div",{"class":"tablo-senaryosu"})
all_points = soup.find_all("td",{"class":"col10"})

for job in all_jobs:
    print(job.tr.text)

for point in all_points:
    print(job.td.text)

# all_jobs = soup.find_all("p",{"class":"h2 m-0 entryWinner pb-std pb-md-0"})

# for job in all_jobs:
#     print(job.a.text)

# all_data = soup.find_all("div",{"class":"col-6 col-lg-4 dataPoint"})

# for data in all_data:
#     print(data.text)