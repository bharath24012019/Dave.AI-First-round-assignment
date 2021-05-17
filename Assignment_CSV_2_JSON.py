#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import json


# In[40]:


#df1 is the dataframe of customer_data_one.csv and df2 is the dataframe of the customer_data_two.csv

df1 = pd.read_csv("customer_data_one.csv")
df2 = pd.read_csv("customer_data_two.csv")


# In[41]:


#df5 is the data frame in which outdated values of customer is removed
#append is first used to club the two data frames(ie two csv file's records)
#drop_duplicates is used to remove the outdated rows or records
#sort_values is used to sort the data frame based in the first name


df5 = df1.append(df2, ignore_index = True).drop_duplicates(subset = "mobile_number", keep = "last", inplace = False)
df5 = df5.sort_values(by=['first_name'])


# In[46]:


#customer_data is a dictionary that contains the details of the customer
#In data_json mobile number is added as the key and customer_data is used as the value
#data_json is the JSON Object

customer_data = [  dict([ (colname, row[i])  for i,colname in enumerate(df5.columns)  ]) for row in df5.values ]
data_json = dict()
for rows in customer_data:
    key = str(rows['mobile_number'])
    data_json[key] = rows
    
#data_json_arr is the JSON Array of the JSON Object
    
data_json_arr = dict()
data_json_arr["Customer Data"] = data_json


# In[43]:


#The JSON data is written into a file data.txt

with open('data.txt', 'w') as outfile:
    json.dump(data_json_arr, outfile)

