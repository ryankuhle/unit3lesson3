from bs4 import BeautifulSoup
import requests

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

def getCleanInsert(url):
    '''getCleanInsert
    Take URL as parameter. Clean data. Insert into SQLite table.
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    table = soup('table')[6]

    for row in table.findAll('tr')[8:191]:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        country = cols[0]
        year = cols[1]
        men = int(cols[7])
        women = float(cols[10])
        total = (men + women) / 2
        print "%s, %s, %s, %s, %s" % (country, year, total, men, women)

getCleanInsert(url)
