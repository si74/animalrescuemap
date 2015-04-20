import sys
from bs4 import BeautifulSoup
import urllib2

link = "http://www.animalalliancenyc.org/about/apos/atoz.htm"

page = urllib2.urlopen(link)

#set up beautiful soup
soup = BeautifulSoup(page.read())

tags = soup.findAll(attrs={'class':'apochartname'})

#write results to text file
import csv

f = open('APO.txt','w')

is_new_item = True

for tag in tags:
	if tag.findChildren():
   		if tag.findAll(text=True):
   			if tag.string:
   				print tag.string
   				f.write(tag.string.encode('ascii','ignore'))
   			else:
   				print tag.contents[0]	
   				f.write(tag.contents[0].encode('ascii','ignore'))
		else:
   			subtags = tag.findChildren('a')
   			for sub in subtags:
   				print sub.get('href')
   				f.write(","+sub.get('href').encode('ascii','ignore'))
   			f.write('\n')
	else:
   		print tag
		f.write(tag.string)

f.close()