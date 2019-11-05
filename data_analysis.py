#!/usr/bin/env python
# coding: utf-8

# In[5]:


from enum import Enum
from string import punctuation, whitespace, digits
import itertools as it


# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel("https://minio.apps.selfip.com/mymedia/xlxs/NCPDP.xlsx")


# In[11]:


# Create variables to use as column names using enums.
translation = str.maketrans(dict(zip((*punctuation, *whitespace), it.cycle("_"))))


# In[13]:


Columns = Enum(
    "Columns",
    type=str,
    names=zip((item.translate(translation).upper() for item in df.columns), df.columns),
)


# In[17]:


Columns.__members__


# In[19]:


globals().update(Columns.__members__)  # Not the best practice. It is convenient!


# In[20]:


df[
    [
        any(f"Schedule {schedule}" in item for schedule in ("I", "II"))
        for item in df[NCPDP_PREFERRED_TERM]
    ]
]


# In[21]:


df.shape


# In[22]:


df[NCPDP_PREFERRED_TERM]


# In[ ]:




