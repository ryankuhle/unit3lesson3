from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
import csv

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

con = lite.connect('education.db')

def create_table():
    '''create_table
    Create SQLite table to store education data in.
    '''
    cur = con.cursor()
    with con:
        cur.execute('CREATE TABLE life_expectancy (country TEXT, year INT, male    INT, female INT)')
    print "Table creation successful."

def get_edu_data(url):
    '''get_edu_data
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
        female = int(cols[10])
        info = (country, year, male, female)
        cur = con.cursor()
        with con:
            cur.execute('INSERT INTO life_expectancy (country, year, male, female) VALUES (?,?,?,?)', info)
        print "Inserting data for: %s" % (country)

def get_gdp_data():
    '''get_gdp_data
    Parse GDP data from CSV and insert into SQLite table.
    '''
    with open('ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
        next(inputFile) # skip the first four lines
        next(inputFile)
        next(inputFile)
        next(inputFile)
        header = next(inputFile)
        inputReader = csv.reader(inputFile)
        #cur = con.cursor()
        for line in inputReader:
            print '"' + line[0] + '","' + '","'.join(line[42:-5]) + '"'
        #    with con:
        #        cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-5]) + '");')


#Run these functions ONCE upon initial setup
##create_table()
##get_edu_data(url)
get_gdp_data()

# we are trying to compare school life expectancy against national GDP
# need to figure out what columns I want from CSV: country name, all data from 1999 through 2010
