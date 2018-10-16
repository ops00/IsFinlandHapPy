#!/usr/env/bin python3.6
# -*- coding: utf-8 -*-

import urllib.request
import bs4 as bs

#Create simple wordlist, that is easy to add to a Python list. 

source = urllib.request.urlopen("https://www.is.fi/rss/kotimaa.xml").read()
soup = bs.BeautifulSoup(source, "xml")
titles = soup.find_all("title")

for title in titles:
	oneArt = title.string.split()
	oA = "',\n'".join(oneArt)
	print(oA)
	with open ("wordlist.py", "a") as f:
		f.write(oA)
		f.close()
