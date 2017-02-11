#proj2.py
import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
#http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
for story_heading in soup.find_all(class_="story-heading")[:10]: 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

### Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')
base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
divtags = soup.find_all('div', class_ = 'view-most-read')
for tag in divtags:
	litags = tag.find_all('li')
	for litag in litags:
		print(litag.text)
# http://stackoverflow.com/questions/13202087/beautiful-soup-find-children-for-particular-div

### request assistance to make this use children instead of the double-loop


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
