import requests
from bs4 import BeautifulSoup


fhand = open("testdetailspage.html")
html = fhand.read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)
em = soup.find('div', class_ = 'field-type-email')
emdivs = em.find_all('div', class_ = 'field-item')
for div in emdivs:
	print(div.get_text())
