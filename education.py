#table has five usable columns
#Country | Year | Total | Men | Women

#class of the row that I want is: tcont
"""example row that I need
<tr class="tcont">
<td height="19">Albania</td>
<td align="right" height="19">2004</td>
<td height="19"> </td>
<td height="19">a</td>
<td align="right" height="19">11</td>
<td></td>
<td height="19"></td>
<td align="right" height="19">11</td>
<td></td>
<td height="19"></td>
<td align="right" height="19">11</td>
<td height="19"></td>
</tr>

I want the data in columns: 0, 1, 4, 7, 10
"""

from bs4 import BeautifulSoup
import requests

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content)
table = soup('table')[6] #full table  of content that we want
table_rows = table.findAll('tr') #,all of the rows that we want
table_rows = table_rows[8:191] #rows containing the data that we want

data = []
#table = soup.find('table', attrs={'class':'lineItemsTable'})
#table_body = table.find('tbody')

rows = table.findAll('tr')[8:191]
for row in rows:
    cols = row.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

print data
#for rows in table_rows:
#    rows = rows.rstrip('</tr>')
#    print rows
#    plit by td tag
#    Insert into database
