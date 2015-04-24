#Note: must grab fuzzy string matching library from github: 
# https://github.com/seatgeek/fuzzywuzzy
#Note: install python levenshtein
#https://pypi.python.org/pypi/python-Levenshtein/
#
import json
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from urlparse import urlparse

#Open all the relevant files
with open('petfinderList.json') as pet_file:
	pet_data = json.load(pet_file)

with open('APOlist.csv','rU') as apo_file:
	apo_data = csv.reader(apo_file,dialect=csv.excel_tab)
	apos = []
	for row in apo_data:
		print row
		#apo_row = row.split(',')
		#apo = {}
		#apo['name'] = apo_row[0]
		#for x in range(1,(len(apo_row)-1)):



with open('NewHopelist.csv','rU') as hope_file:
	hope_data = csv.reader(hope_file, dialect=csv.excel_tab)
	newhopes = []
	for row in hope_data:
		newhopes.append(row[0])

with open('n_zipcodes.csv','rU') as zip_file:
	zipcode_data = csv.reader(zip_file, dialect=csv.excel_tab)
	zipcodes = []
	for row in zipcode_data:
		zipcodes.append(int(row[0]))


shelter_list = pet_data['petfinder']['shelters']['shelter']

shelter_count = 0
hope_count = 0 

final_list = []

for shelter in shelter_list: 

	#only considering rescues geographically located in NYC
	if ( int(shelter['zip']['$t']) in zipcodes):

		final = {}

		final['id'] = shelter['id']['$t']
		final['name'] = shelter['name']['$t']
		final['new_hope'] = False

		if not shelter['phone']: 
			final['phone'] = ''
		else:
			final['phone'] = shelter['phone']['$t']

		if not shelter['email']:
			final['email'] = ''
		else:
			final['email'] = shelter['email']['$t']

		final['latitude'] = shelter['latitude']['$t']
		final['longitude'] = shelter['longitude']['$t']

		if not shelter['address1']:
			final['address1'] = ''
		else:
			final['address1'] = shelter['address1']['$t']

		if not shelter['address2']:
			final['address2'] = ''
		else:
			final['address2'] = shelter['address2']['$t']

		final['city'] = shelter['city']['$t']
		final['state'] = shelter['state']['$t']
		final['zip'] = shelter['zip']['$t']

		shelter_count = shelter_count + 1

		#check which of these are New Hope Partners
		for hope in newhopes: 

			if (fuzz.partial_ratio(shelter['name']['$t'],hope) > 90):

				final['new_hope'] = True

				hope_count = hope_count + 1





print shelter_count
print hope_count