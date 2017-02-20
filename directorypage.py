import requests
from bs4 import BeautifulSoup


fhand = open("testdirectorypage.html")
html = fhand.read()
soup = BeautifulSoup(html, 'html.parser')

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

def findaboutURLs(html, tag, tagclass):
	"""
	Usage: takes a BeautifulSoup-formatted html page, the tag to find, and the class of that tag
	Returns a list of relative path URLs based on the "about" attribute
	"""
	# details = soup.find_all('div', class_ = 'field-item')
	sites = []
	divs = html.find_all(tag, class_ = tagclass)
	for i in divs:
		# print(i)
		if i.has_attr('about'):
			page = i['about']
			print("******")
			sites.append(page)
	return(sites)


def findemails(soup, addrlist):
	"""
	Takes BeautifulSoup-formatted html and looks for email addresses.  
	Returns list of these email addresses
	"""
	em = soup.find('div', class_ = 'field-type-email')
	emdivs = em.find_all('div', class_ = 'field-item')
	for div in emdivs:
		print(div.get_text())
		addrlist.append(div.get_text())
	return addrlist

def parsesoup(page):
	"""
	Takes the specific page /people/person-name, forms the directory URL, 
	accesses this page and creates soup file for it.
	"""
	base_url = "https://www.si.umich.edu"
	new_url = base_url + page
	print(new_url)
	#r = requests.get(new_url,headers={'User-Agent': 'Mozilla/5.0'})
	# soup = BeautifulSoup(r.text, 'html.parser')
	fhand = open("testdetailspage.html")
	html = fhand.read()
	soup = BeautifulSoup(html, 'html.parser')
	fhand.close()
	return soup

# ems = findemails(soup, 'div', 'views-row')
emURLs = findaboutURLs(soup, 'div', 'node-person')
print(emURLs)
emailaddresses = []
for person in emURLs:
	 findemails(parsesoup(person), emailaddresses)

print('test complete')


#Look for second page
newpage = nextpagecheck(soup, 'li', 'pager-next')
pagecount = 1
#Parse remaining pages
# while newpage:
# 	pagecount += 1
# 	# print(newpage)
# 	r = requests.get(newpage,headers={'User-Agent': 'Mozilla/5.0'})
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	# findaboutURLs(soup, 'div', 'field-item')
# 	findaboutURLs(soup, 'div', 'views-row')
# 	newpage = nextpagecheck(soup, 'li', 'pager-next')

print("{} pages found".format(pagecount))
print(newpage)