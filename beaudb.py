#!/usr/env/bin python3.6
# -*- coding: utf-8 -*-

 
import urllib.request
import bs4 as bs
import pymysql
import plist
import nlist

#Is Finland positive?

source = urllib.request.urlopen("https://www.is.fi/rss/tuoreimmat.xml").read()

soup = bs.BeautifulSoup(source, "xml")

titles = soup.find_all("title")

def newsCheck(numberOfArt):
	controlNumber = 1
	newsCheck.positiveNews = 0
	newsCheck.negativeNews = 0
	
	for title in titles:
		if controlNumber < numberOfArt:
			oneArt = title.string.split()
			controlNumber += 1
			for word in oneArt:
				if word in plist.poslist is not None:
					newsCheck.positiveNews += 1

				elif word in nlist.neglist is not None:
					newsCheck.negativeNews += 1
					
				else:
					pass
		else:
			exit()
			

def databaseUpdate():
	try:
		conn = pymysql.connect(host="xx",
								user="xx",
								password="xx",
								db="xx")
		cursor = conn.cursor()
		val = (positivityValue)
		sql = ("UPDATE positivity SET POSITIVITYVAL = %s WHERE ID = 1")
		cursor.execute(sql, val)
		conn.commit()
		cursor.close()
		conn.close()
	except Exception as error:
		print(error)
		print("error")

def pValues():
	try:
		pv = (newsCheck.positiveNews/(newsCheck.positiveNews + newsCheck.negativeNews)*100)
		return pv;
	except ZeroDivisionError as e:
		print(e)
		return 0;
	

newsCheck(50)
positivityValue = pValues()
#databaseUpdate()
print("Positivity level of Finland today:", positivityValue ,"%")
