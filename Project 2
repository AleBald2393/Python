!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y 
!pip install lxml==4.6.4
!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Steps for extracting the data¶
#Send an HTTP request to the web page using the requests library.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text
print(data)

#Parse the HTML content of the web page using BeautifulSoup.


#Identify the HTML tags that contain the data you want to extract.
#Use BeautifulSoup methods to extract the data from the HTML tags.
#Print the extracted data

What is parsing?
In simple words, parsing refers to the process of analyzing a string of text or a data structure, usually following a set of rules or grammar, to understand its structure and meaning. Parsing involves breaking down a piece of text or data into its individual components or elements, and then analyzing those components to extract the desired information or to understand their relationships and meanings.

soup = BeautifulSoup(data, 'html5lib')

PASO3:
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

Working on HTML table ¶

These are the following tags which are used while creating HTML tables.

<table>: This tag is a root tag used to define the start and end of the table. All the content of the table is enclosed within these tags.

<tr>: This tag is used to define a table row. Each row of the table is defined within this tag.

<td>: This tag is used to define a table cell. Each cell of the table is defined within this tag. You can specify the content of the cell between the opening and closing tags.

<th>: This tag is used to define a header cell in the table. The header cell is used to describe the contents of a column or row. By default, the text inside a tag is bold and centered.

<tbody>: This is the main content of the table, which is defined using the tag. It contains one or more rows of elements.

PASO4:
We will use find() and find_all() methods of the BeautifulSoup object to locate the table body and table row respectively in the HTML.

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
PASO5:
#imprimir los datos
netflix_data.head()

AHORA CON PANDAS
read_html_pandas_data = pd.read_html(url)
#Or you can convert the BeautifulSoup object to a string.
read_html_pandas_data = pd.read_html(str(soup))

netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head()

#Para traer el titulo de las columnas
list(amazon_data.columns)

#para traer el último dato de x columna, en esta caso "Open"
amazon_data["Open"].iloc[-1]
