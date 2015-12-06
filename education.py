from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
import csv

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

con = lite.connect('education.db')

def create_tables():
    '''create_tables
    Create SQLite tables to store education and GDP data in, respectively.
    '''
    cur = con.cursor()
    with con:
        cur.execute('CREATE TABLE life_expectancy (country TEXT, year INT, male    INT, female INT)')
        print "Created life_expectancy table successfully."
        cur.execute('CREATE TABLE gdp (country TEXT, _1999 TEXT, _2000 TEXT, _2001 TEXT, _2002 TEXT, _2003 TEXT, _2004 TEXT, _2005 TEXT, _2006 TEXT, _2007 TEXT, _2008 TEXT, _2009 TEXT, _2010 TEXT)')
        print "Created gdp table successfully."

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
        cur = con.cursor()
        for line in inputReader:
            info = (line[0], line[43], line[44], line[45], line[46], line[47], line[48], line[49], line[50], line[51], line[52], line[53], line[54])
            with con:
                cur.execute('INSERT INTO gdp (country, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);', info)


#Run these functions ONCE upon initial setup
##create_tables()
##get_edu_data(url)
##get_gdp_data()
