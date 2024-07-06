#!/usr/bin/env python
# coding: utf-8

# ## Write code to Check if two strings are Anagram or not
# An anagram is a word or phrase that's formed by rearranging the letters of another word or phrase.

# In[1]:


a=input("enter string1:") #taking input as string from user and assigning it to a variable a

b=input("enter string2:") #taking input as string from user and assigning it to a variable b
if len(a)!=len(b): #checking length of strings using len function and comparing both strings 
    print("strings are not anagram")
else:
    a=sorted(a) #sorted function is used to sort string by characters
    b=sorted(b)
if a==b: #check if now strings are  matches 
    print("strings are anagram")
else:
    print("strings are not anagram")


# In[ ]:





# In[ ]:




