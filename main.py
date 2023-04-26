import requests
from bs4 import BeautifulSoup
import csv

# provide the website link
url = 'https://www.example.com/'

# send a GET request to the website
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the links on the webpage
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

# create a CSV file and write the links to it
with open('links.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Links'])
    for link in links:
        writer.writerow([link])

print('Data saved in links.csv')
