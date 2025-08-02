
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://internshala.com/internships/python-internship"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

# Check response status
if response.status_code== 200:
    print("Website accessed successfully!\n")
else:
    print("Failed to access website.Status code: ", response.status_code)

# HTML parse
soup = BeautifulSoup(response.text, "html.parser")

# Job cards
job_cards = soup.find_all("div", class_="individual_internship")

jobs_data = []

for job in job_cards:

    title_tag = job.find('a', class_='job-title-href')
    job_title = title_tag.text.strip() if title_tag else "N/A"

    company_tag = job.find('p', class_='company-name')
    company = company_tag.text.strip() if company_tag else "N/A"

    location_container = job.find('div', class_='row-1-item locations')
    location_tag = location_container.find('a') if location_container else None
    location = location_tag.text.strip() if location_tag else "N/A"

    jobs_data.append([job_title, company, location])

df = pd.DataFrame(jobs_data, columns=['Job Title ', 'Company ', 'Location '])

# save to CSV
df.to_csv('internshala_jobs.csv', index=False)

print(f" Total Jobs Scraped: {len(jobs_data)} ")
print("CSV file created successfully!")

