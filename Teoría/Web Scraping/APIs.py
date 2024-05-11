The advantages of using APIs:

Automation. Less human effort is required and workflows can be easily updated to become faster and more
productive.
Efficiency. It allows to use the capabilities of one of the already developed APIs than to try to independently implement some functionality from scratch.

The disadvantage of using APIs:
Security. If the API is poorly integrated, it means it will be vulnerable to attacks, resulting in data breeches or losses having financial or reputation implications.

Another example of simple API we will use in this notebook is Fruityvice application. The Fruityvice API web service which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The web service is completely free to use and contribute to.

Get Methods
get_cell()
get_city()
get_dob()
get_email()
get_first_name()
get_full_name()
get_gender()
get_id()
get_id_number()
get_id_type()
get_info()
get_last_name()
get_login_md5()
get_login_salt()
get_login_sha1()
get_login_sha256()
get_nat()
get_password()
get_phone()
get_picture()
get_postcode()
get_registered()
get_state()
get_street()
get_username()
get_zipcode()


#To start using the API you can install the randomuser library running the pip install command.
!pip install randomuser
from randomuser import RandomUser
import pandas as pd

r = RandomUser()

#Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
some_list

#For example, to get full name, we call get_full_name() function
name = r.get_full_name()

#generate photos of the random 10 users.
for user in some_list:
    print (user.get_picture())

#Obtener una tabla con información completa de usuarios
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     
get_users()
df1 = pd.DataFrame(get_users())  

Fruityvice API
#Another, more common way to use APIs, is through requests library.
import requests
import json

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)

pd.DataFrame(results)

df2 = pd.json_normalize(results)
df2

#Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

Official Joke API
his API returns random jokes from a database. The following URL can be used to retrieve 10 random jokes.

https://official-joke-api.appspot.com/jokes/ten

Using requests.get("url") function, load the data from the URL.

import requests
jokes= requests.get("https://official-joke-api.appspot.com/jokes/ten")

results = json.loads(jokes.text)

#Convert json data into pandas data frame. Drop the type and id columns.
df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
df3
