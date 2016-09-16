from usingenglish.idiomextractor import *
import string
import csv
url = "http://www.usingenglish.com/reference/idioms/%s.html"
alphabet = string.ascii_lowercase[:26]
base_url = "http://www.usingenglish.com"
total_idioms = []
with open('idioms.csv', 'a') as csvfile:
    fieldnames = ['idiom', 'definition']
    idiomwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    idiomwriter.writeheader()
    for al in alphabet:
        scrape_url = url%(al)
        page_links = getpaginationlink(base_url, scrape_url)
        for link in page_links:
            idiom_list = getidioms(link)
            for idiom in idiom_list:
                try:
                    idiomwriter.writerow(idiom)
                except Exception:
                    print("-----------------------Error Occorred---------------------")
                print(idiom)
                total_idioms.append(idiom)


print(len(total_idioms))
