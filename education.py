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
table = soup('table')[6]

data = []

#rows = table.findAll('tr')[8:191]
for row in table.findAll('tr')[8:191]:
    cols = row.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    country = cols[0]
    year = cols[1]
    men = int(cols[7])
    women = float(cols[10])
    total = (men + women) / 2
    print "%s, %s, %s, %s, %s" % (country, year, total, men, women)
    #cols = [ele.text.strip() for ele in cols]
    #data.append([ele for ele in cols if ele])
    #some items have 5 columns, some have 6. Need to eliminate unneeded column
