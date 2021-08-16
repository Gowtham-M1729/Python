#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


def getdata(url):
	r = requests.get(url)
	return r.text


# In[3]:


# link for extract html data
htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all("div", class_="gold_silver_table")
print(result)


# In[9]:


# Declare string var
# Declare list
mydatastr = ''
result = []

# searching all tr in the html data
# storing as a string
for table in soup.find_all('tr'):
    mydatastr += table.get_text()

# set accourding to your required
mydatastr = mydatastr[1:]
itemlist = mydatastr.split("\n\n")

for item in itemlist[:-8]:
    result.append(item.split("\n"))

result


# In[5]:


# Calling DataFrame constructor on list
df = pd.DataFrame(result[:-8])
df


# In[13]:


result = soup.find_all("div", class_="gold_silver_table")
print(result)


# In[ ]:




