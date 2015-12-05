from bs4 import BeautifulSoup
import requests
import sqlite3 as lite

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

def createTable():
    '''createTable
    Create SQLite table to store education data in.
    '''
    con = lite.connect('education.db')
    cur = con.cursor()
    with con:
        cur.execute('CREATE TABLE life_expectancy (id INT PRIMARY KEY, country TEXT, year INT, male INT, female INT)')
    print "Table creation successful."

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
        year = int(cols[1])
        male = int(cols[7])
        female = float(cols[10])
        print "%s, %s, %s, %s" % (country, year, male, female)

createTable()

getCleanInsert(url)
