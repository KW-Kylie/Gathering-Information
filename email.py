from bs4 import BeautifulSoup
import re
import requests
import requests.exceptions
import urlparse
from collections import deque

# List of urls to be crawled
urls = deque(['https://www.google.com/'])

# URLs that we have already crawled
scraped_urls = set()

# Crawled emails
emails = set()

# Scrape urls one by one queue is empty
while len(urls):
	url = urls.popleft()
	scrapped_urls.add(url)
	
	# Get base url
	part= urlparse.urlsplit(url)
	base_url = "{0.scheme}://{0.netloc}".format(parts)
	path = url[:url.rfind('/')+1] if '/' in parts.path else url

	# get url's content
	print("Scraping %s" % url)
	try:
		response = request.get(url)
	except (requests.exceptions.MissingSchema, requrests.exceptions.ConnectionError):
		continue

	# Search e-mail addresses and add them into the output set
	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
	emails.update(new_emails)

	# find and process all the anchors
	for anchor in soup.find_all("a"):
		
		# extract link url
		link = anchor.attrs["href"] if "href" in anchor.attrs else ''
		
		# resolve relative links
		if link.startswith('/'):
			link = base_url + link
		elif not link.startswith('http'):
			link = path + link
		
		# add the new url to the queue if not link in urls and not link in scraped_urls:
		else urls.append(link)