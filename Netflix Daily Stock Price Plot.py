#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[3]:


#Reading CSV Files
netflix_stocks = pd.read_csv("Desktop/NFLX.csv")
print(netflix_stocks)


# In[4]:


#Changing "Adj Close" to "Price"
netflix_stocks.rename(columns={"Adj Close" : "Price"}, inplace=True)


# In[12]:


#Creating a Violin Plot
ax = sns.violinplot()
sns.violinplot(data=netflix_stocks, x="Date", y="Price")

ax.set_title("Distribution of 2023 Netflix Stock Prices Daily")
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Dates in 2023")
plt.show()


# In[ ]:




