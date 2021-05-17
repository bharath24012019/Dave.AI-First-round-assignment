#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import json


# In[ ]:


#df1 is the dataframe of customer_data_one.csv and df2 is the dataframe of the customer_data_two.csv

df1 = pd.read_csv("customer_data_one.csv")
df2 = pd.read_csv("customer_data_two.csv")


# In[ ]:


#df5 is the data frame in which outdated values of customer is removed
#append is first used to club the two data frames(ie two csv file's records)
#drop_duplicates is used to remove the outdated rows or records
#sort_values is used to sort the data frame based in the first name


df5 = df1.append(df2, ignore_index = True).drop_duplicates(subset = "mobile_number", keep = "last", inplace = False)
df5 = df5.sort_values(by=['first_name'])


# In[ ]:


#customer_data is the JSON Object

customer_data = dict()
for row in df5.values:
    customer_data[row[8]] = row 


# In[ ]:


#data_json_arr is the JSON Array of the JSON Object
    
data_json_arr = dict()
data_json_arr["Customer Data"] = customer_data


# In[ ]:


#The JSON data is written into a file data.txt

with open('data1.txt', 'w') as outfile:
    json.dump(data_json_arr, outfile)

