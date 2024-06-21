#!/usr/bin/env python
# coding: utf-8

# ### loops in python
# 
# * while loop -->In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.
# 
# * for loop --> A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# In[1]:


count = 0
while (count < 3):
    count = count + 1
    print("Hello")


# ### Using else with While Loop -->
# 
# The else clause is only executed when your while condition becomes false. If you break out of the loop, or if an exception is raised, it won’t be executed. 
# 
# Syntax :
# 
# while condition:
# 
#      # execute these statements
#      
# else:
# 
#     #execute these statements

# In[2]:


count = 0
while (count < 3):
    count = count + 1
    print("Hello")
else:
    print("this is Else Block")


# ### for loop

# In[4]:


n = 4
for i in range(0, n):
    print(i)


# In[5]:


a=[1,2,3,4,5]
for i in a:
    print(i)


# In[6]:


for i in a:
    i=i+2
    print(i)
    


# In[7]:


list = ["apple", "mango", "grapes"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")


# In[ ]:




