#!/usr/bin/env python
# coding: utf-8

# # 1: View and add the dataset

# In[ ]:


#Import the necessary library
import numpy as np


# In[ ]:


#manually add the summer olympics, london 2012 dataset as arrays
np_olympics_country = np.array(['GBR','CHN','RUS','US','KOR','JPN','GER'])
np_olympic_country_Gold = np.array([29,38,24,46,13,7,11])
np_olympic_country_Silver = np.array([17,28,25,28,8,14,11])
np_olympic_country_Bronze = np.array([19,22,32,29,7,17,14])


# # 2: Find the country with maximum gold medals

# In[ ]:


#use the argmax() method to find the highest number of gold medals
max_gold_index = np_olympic_country_gold.argmax()


# In[ ]:


country_with_max_gold = np_olympic_country[max_gold_index]


# In[ ]:


#print the name of the country
print(country_with_max_gold)

us
# # Find the countries with more than 20 gold medals

# In[ ]:


#use Boolean indexing technique to find the required output
print(np_olympic_country[np_olympic_Country_Gold>20])

['GBR' 'CHN' 'RUS' 'US'
# # Evaluate the dataset and print the name of each country with its gold medals and total number of medals

# In[ ]:


#use a for loop create the required output
#print each country name with number of gold medals
#print each country name with total number of medals
for i in range(len(np_olympic_country));
    gold_medal = np_olympic_COuntry_Gold[i]
    Country = np_olympic_country[i]
    total_medal = np_olympic_country_Bronze[i]+np_olympic_country_Gold[i]+np_olympic_country_Gold[i]+np_olympic_country_Silver[i]
    print('{}, gold_medal {}, Total medals{}'.format(Country,gold_medal,total_medal) )

GBR, gold_medal 29, Total medals 65
CHN, gold_medal 38, Total medals 88
RUS, gold_medal 24, TOtal medals 81
US,  gold_medal 13, Total medals 28
JPN, gold_medal 7,  Total medals 38
GER, gold_medal 11, Total medals 36