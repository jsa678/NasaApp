import requests
import time
import re
from bs4 import BeautifulSoup

scienceUrl = "https://www.sciencenews.org/topic/space"

# <class 'bs4.element.Tag'>
def scrapeSite(url):
	html_text = requests.get(scienceUrl).text
	soup = BeautifulSoup(html_text, 'html.parser')
	title = soup.find_all("h3",{"class":"post-item-river__title___vyz1w"})
	#title = soup.select("h3",{"class":"widget-post-list-item__title___XGFHE"})
	titleOnly = []
	linksOnly = []
	for article in title:
		print(article)
		article.select(".attributes-value span")
		print(article.find('a').get('href',''))
		print(article.get_text())
		link = article.find('a').get('href','')
		articleTitle = article.get_text()
		tempArray = [articleTitle,link]
		titleOnly.append(articleTitle)
		linksOnly.append(link)
		print("_________________________________")
	return titleOnly, linksOnly


titleAll, linkAll = scrapeSite(scienceUrl)