#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assigning the string
Hours="thirsty"
print(Hours)


# In[17]:


#indexing using string
days="thirty days"
print(days[0])
print(days[5])
      


# In[6]:


#to print particular character from certain text
challenge="i will win"
print(challenge[7:10])


# In[7]:


#print the length of the character
challenge="i will win"
print(len(challenge))


# In[9]:


#convert string into lower character
challenge="I WILL WIN"
print(challenge.lower())


# In[10]:


#adding spaces during concatination
a="30 days"
b="30 hours"
c=a + " " + b
print(c)


# In[14]:


#casefold()-usage
text="Thirty days and thirty hours"
x=text.casefold()
print(x)


# In[13]:


text="thirty days and thirty hours"
x=text.capitalize()
print(x)


# In[15]:


text="thirty days and thirty hours"
x=text.isalpha()
print(x)


# In[16]:


text="thirty days and thirty hours"
x=text.isalnum()
print(x)


# In[ ]:
