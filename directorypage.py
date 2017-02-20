import requests
from bs4 import BeautifulSoup



# Function definitions
def nextpagecheck(html, tag, tagclass):
	"""
	Usage: takes a BeautifulSoup-formatted html page, the tag to find, and the class of that tag.
	Returns the (first) anchor text (a href) of a tag with that class.
	"""
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
	Usage: takes a BeautifulSoup-formatted html page, the tag to find, and the class of that tag.
	Returns a list of relative path URLs based on the "about" attribute.
	"""
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
	Returns list of these email addresses.
	"""
	em = soup.find('div', class_ = 'field-type-email')
	emdivs = em.find_all('div', class_ = 'field-item')
	for div in emdivs:
		print(div.get_text())
		addrlist.append(div.get_text())
	return addrlist

def parsesoup(page):
	""" 
	Accesses a website and creates soup file for it.
	"""
	r = requests.get(page,headers={'User-Agent': 'Mozilla/5.0'})  #commented out for testing during 403 error
	if r.status_code == 403:
		print('403 error, try again later')
		return None
	soup = BeautifulSoup(r.text, 'html.parser')  #commented out while testing during 403 error
	print(soup)
	# fhand = open("testdetailspage.html")
	# html = fhand.read()
	# soup = BeautifulSoup(html, 'html.parser')
	# fhand.close()
	return soup

def wrapper(html, adrlist):
	"""
	Look at the BeautifulSoup-formatted html file, find any details pages in the soup,
	Scrape the email addresses from all details files on that page.
	""" 
	emURLs = findaboutURLs(html, 'div', 'node-person')
	print(emURLs)
	base_url = 'http://si.umich.edu'
	# For each path provided, create a URL, parse the URL, and add to the email address list
	for person in emURLs:
		new_url = base_url + person
		print(new_url)
		test = findemails(parsesoup(new_url), adrlist)
		# print(test)
	#return test

#Open and parse the first page
# fhand = open("testdirectorypage.html")
# html = fhand.read()
# soup = BeautifulSoup(html, 'html.parser')
base_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
soup = parsesoup(base_url)  #commented out for testing during 403 error
print(soup)


emailaddresses = []
emailaddresses = wrapper(soup, emailaddresses)


# Look for second page
newpage = nextpagecheck(soup, 'li', 'pager-next')
pagecount = 1
#Parse remaining pages
while newpage:
	pagecount += 1
	soup = parsesoup(newpage)
	# print(soup)
	emailaddresses = wrapper(soup, emailaddresses)
	# print("test*******")
	try:
		newpage = nextpagecheck(soup, 'li', 'pager-next')
	except AttributeError as e:
		newpage	= False
		print('Error - page did not load properly: ', e)
print(emailaddresses)

print("{} pages found".format(pagecount))
# print(newpage)