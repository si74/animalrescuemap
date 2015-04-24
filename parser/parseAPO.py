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

#f = open('APO.txt','w')

is_new_item = True

for tag in tags:
   if tag.findChildren():
      if tag.findAll(text=True):
         if tag.string:
            sys.stdout.write(tag.string)
         else:
            sys.stdout.write(tag.contents[0])
      else:
         subtags = tag.findChildren('a')
         for sub in subtags:
            sys.stdout.write("\t"+sub.get('href'))
         sys.stdout.write("\n")
   else:
      sys.stdout.write(str(tag))