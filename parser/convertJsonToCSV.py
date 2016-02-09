import json
import csv

zipcodes = []

with open('n_zipcodes.csv','rU') as zip_file:
	zipcode_data = csv.reader(zip_file, dialect=csv.excel_tab)
	for row in zipcode_data:
		zipcodes.append(int(row[0]))

with open('petfinderList.json') as data_file:    
    data = json.load(data_file)

    rescues = data['petfinder']['shelters']['shelter'];

    with open('petfinderList.csv', 'w') as file:
		
		spamwriter = csv.writer(file, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
		num = 0

		spamwriter.writerow(["Name","Email","Phone","Address1","Address2"])

		for rescue in rescues:

			name = rescue['name']['$t']

			#grab email
			if (rescue['email']):
				email = rescue['email']['$t']
			else:
				 email = ""

			#grab phone number
			if (rescue['phone']):
				phone = rescue['phone']['$t']
			else:
				phone = ""

			#grab zipcode
			zipcode = rescue['zip']['$t']
			if (int(zipcode) not in zipcodes):
				continue

			if (rescue['address1']):
				address1 = rescue['address1']['$t']
			else:
				address1 = ""

			if (rescue['address2']):
				address2 = rescue['address2']['$t']
			else:
				address2 = ""

			spamwriter.writerow([name,email,phone,address1,address2])

			num += 1
			print num

