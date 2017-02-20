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

# def findemails(html, tag, tagclass):
# 	# details = soup.find_all('div', class_ = 'field-item')
# 	details = html.find_all(tag, class_ = tagclass)
# 	for child in details.children:
# 		print(child, type(child))
		
# 		print("******")




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

print("{} pages found".format(pagecount))
print(newpage)