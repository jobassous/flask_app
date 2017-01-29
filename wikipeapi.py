from wikiapi import WikiApi
wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'en'}) # to specify your locale, 'en' is default

results = wiki.find('Donald Trump') = ['Donald_Trump', 'Donald_Trump_presidential_campaign,_2016']
article = wiki.get_article(results[0])

for article in results.articles:
	print(article.heading, article.url)
