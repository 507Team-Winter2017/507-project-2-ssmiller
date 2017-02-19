#proj2.py
import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
### Your Problem 1 solution goes here

#http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
for story_heading in soup.find_all(class_="story-heading")[:10]: 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())




#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
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
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')
pics = soup.find_all('img')
for picture in pics:
	print(picture.get('alt',"No alternative text provided!"))
# why doesn't "alt" in picture work as a test?


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

# Function definitions
def nextpagecheck(html, tag, tagclass):
	# nextpage = soup.find('li', class_ = 'pager-next')
	root_url = "https://www.si.umich.edu" 
	nextpage = html.find(tag, class_ = tagclass)
	# print(nextpage)
	nextsite = None
	if nextpage.find('a'):
		print("Another page found")
		nextsite = root_url + (nextpage.find('a')['href'])
		return nextsite

def findemails(html, tag, tagclass):
	# details = soup.find_all('div', class_ = 'field-item')
	details = html.find_all(tag, class_ = tagclass)
	for detail in details:
		# if detail.find('a'):
		# 	print("test")
		# 	print(detail)
		print("test")


#First pass through
base_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
  
r = requests.get(base_url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.text, 'html.parser')
# findemails(soup, 'div', 'field-item')
findemails(soup, 'div', 'views-row')

#Look for second page
newpage = nextpagecheck(soup, 'li', 'pager-next')
pagecount = 1
#Parse remaining pages
# while newpage:
# 	pagecount += 1
# 	# print(newpage)
# 	r = requests.get(newpage,headers={'User-Agent': 'Mozilla/5.0'})
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	# findemails(soup, 'div', 'field-item')
# 	findemails(soup, 'div', 'views-row')
# 	newpage = nextpagecheck(soup, 'li', 'pager-next')

# print("{} pages found".format(pagecount))

### Your Problem 4 solution goes here


