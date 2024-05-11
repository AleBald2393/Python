We may use pandas.read_html() function in python to extract all the tables in the web page directly.

We may execute the following lines of code to extract the required table from the web page:
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)

LAB
!pip install html5lib
!pip install bs4

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>

#We can store it as a string in the variable HTML:
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

#We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

TAG
tag_object = soup.title
print("tag object:", tag_object)

print("tag object type:", type(tag_object))

tag_object = soup.h3
tag_object

tag_child = tag_object.b
tag_child

parent_tag = tag_child.parent
parent_tag

is identical to:
tag_object

tag_object parent is the body element.
tag_object.parent

tag_object sibling is the paragraph element.
sibling_1 = tag_object.next_sibling
sibling_1

sibling_2 is the header element, which is also a sibling of both sibling_1 and tag_object
sibling_2 = sibling_1.next_sibling
sibling_2

HTML ATTRIBUTES
tag_child['id']

You can access that dictionary directly as attrs:
tag_child.attrs

We can also obtain the content of the attribute of the tag using the Python get() method.
tag_child.get('id')

Navigable String

tag_string = tag_child.string
tag_string

type(tag_string)

A NavigableString is similar to a Python string or Unicode string. To be more precise, the main difference is that it also supports some BeautifulSoup features. We can convert it to string object in Python:
unicode_string = str(tag_string)
unicode_string

filter
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>

find all methods
table_rows = table_bs.find_all('tr')
table_rows

first_row = table_rows[0]
first_row

#para iterar
for i, row in enumerate(table_rows):
    print("row", i, "is", row)

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('colunm', j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
list_input

Attributes
table_bs.find_all(id="flight")

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input

table_bs.find_all('a', href=True)
