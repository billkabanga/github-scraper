import requests
from bs4 import BeautifulSoup
import csv

#collect the github page
page = requests.get('https://github.com/trending')

#create beautiful soup object
soup = BeautifulSoup(page.text, 'html.parser')

#repo list
repo_box = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

#find all instances of a class
repo_list = repo_box.findAll(class_="Box-row")

# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header
f.writerow(['Developer', 'Repo Name', 'Number of Stars'])

for repo in repo_list:
  #find the first <a> and get the text with dev and repo name
  full_repo_name = repo.find('h1').find('a').text.split('/')

  #get dev name at index 0
  dev_name = full_repo_name[0].strip()

  #get repo name at index 1
  repo_name = full_repo_name[1].strip()

  #get number of stars
  stars = repo.find(class_="octicon octicon-star").parent.text.strip()

  # add the information as a row into the csv table
  f.writerow([dev_name, repo_name, stars])

