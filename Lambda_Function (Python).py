#!/usr/bin/env python
# coding: utf-8

# In[1]:


def test(n,p):
    return n**p


# In[3]:


test(3,2)


# In[4]:


test = lambda n,p:n**p #this is lambda function


# In[6]:


test (3,2)


# In[2]:


add = lambda x,y: x+y


# In[3]:


add(5,4)


# In[4]:


c_to_f = lambda c:(9/5)*c + 32


# In[5]:


c_to_f(45)


# finding max number between two number

# In[7]:


def max(x,y):
    if x >y:
        print(x,"is max number")
    else:
        print(y,"is min number")


# In[8]:


max(5,4)


# In[9]:


finding_max = lambda x,y: x if x>y else y


# In[10]:


finding_max(5,4)


# finding length of string

# In[11]:


s = "Lucky"


# In[12]:


len(s)


# In[13]:


finding_length = lambda s :len(s)


# In[14]:


finding_length(s)


# In[ ]:




