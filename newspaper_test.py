import newspaper

thehindu = newspaper.build('http://www.thehindu.com/')
for article in thehindu.articles:
    print(article.url)


for category in thehindu.category_urls():
    print(category)
