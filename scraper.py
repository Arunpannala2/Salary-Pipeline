import csv
from time import sleep
import json
import requests
from bs4 import BeautifulSoup
import re


def salary_info(job_title, job_city):
    """Extract and return salary information"""
    template = 'https://www.salary.com/research/salary/listing/{}-salary/{}'
 
    # build the url based on search criteria
    url = template.format(job_title, job_city)

    # request the raw html .. check for valid request
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
    except requests.exceptions.ConnectionError:
        return None
   
    # parse the html and extract json data
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(r'Occupation')
    script = soup.find('script', {'type': 'application/ld+json'}, text=pattern)
    json_raw = script.contents[0]
    json_data = json.loads(json_raw)

    # extract salary data
    job_title = json_data['name']
    location = json_data['occupationLocation'][0]['name']

    ntile_10 = json_data['estimatedSalary'][0]['percentile10']
    ntile_25 = json_data['estimatedSalary'][0]['percentile25']
    ntile_50 = json_data['estimatedSalary'][0]['median']
    ntile_75 = json_data['estimatedSalary'][0]['percentile75']
    ntile_90 = json_data['estimatedSalary'][0]['percentile90']

    data = (job_title, location, ntile_10, ntile_25, ntile_50, ntile_75, ntile_90)
    return data


def main(job_title):    
    with open('cities.csv', newline='') as f:
        reader = csv.reader(f)
        cities = [city for row in reader for city in row]
        
    # extract salary data for each city
    salary_data = []
    for city in cities:
        #Enter job title for function
        result = salary_info(job_title, city) 
        if result:
            salary_data.append(result)
            sleep(0.5)
            
    # save data to csv file
    with open('salary-results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title','Location', 'nTile10', 'nTile25', 'nTile50', 'nTile75', 'nTile90'])
        writer.writerows(salary_data)
        
    return salary_data
