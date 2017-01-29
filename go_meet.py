

import random


transport = ["Taxicab",
			"Amtrack",
			"United Airlines",
			"New Jersey Transit",
			"Uber",
			"British Airways",
			"A helicopter",
			"EL AL",
			"LIRR",
			"The Light Rail",
			"The Chunnel",
			"SpaceX",
			"Qantas",
			"Korean Air",
			"The Underground",
			"The Titanic"]


places = ["Paris",
		"London",
		"New York",
		"Las Vegas",
		"Los Angeles",
		"Patterson NJ",
		"Tel Aviv",
		"Dubai",
		"Hong Kong",
		"Mumbai",
		"Sydney",
		"The Moon",
		"Pyongyang",
		"Tehran",
		"Washington D.C.",
		"Moscow",
		"Keasby"]

people = ["Bill DeBlasio",
		"Michael Bloomberg",
		"Barack Hussain Obama",
		"Franklin Delano Roosevelt",
		"Benjamin Netanyahu",
		"Vladmir Putin",
		"Bernie Sanders",
		"Joseph Stalin",
		"Donald J Trump",
		"Herbert Hoover",
		"Winston Churchil",
		"Lou Costello",
		"Derek Jeter",
		"Hillary Clinton",
		"Rabbi Jonathan Sacks",
		"Spencer Rockman",
		"Shlomo Carlebach"]


random_transport = random.choice(transport)
random_place = random.choice(places)
random_person = random.choice(people)

print("I am looking to buy a ticket on %s to go to %s in order to meet %s." % (random_transport, random_place, random_person))