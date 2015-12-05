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
"""

from bs4 import BeautifulSoup
import requests

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content)
table = soup('table')[6]
table_rows = table.findAll('tr') #, { "class" : "tcont" })
table_rows = table_rows[8:191]
print table_rows #Raw data that needs to be split


#split each row  based on probably td tag


#insert content into a pandas
