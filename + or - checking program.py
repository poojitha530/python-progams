#!/usr/bin/env python
# coding: utf-8

# ### positive or negative number

# In[5]:


# using nested if-else  statement
num = 15
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")


# ##### This method uses a nested if-else Statements to check whether a given number is Positive or Negative.
# 
# Algorithm for the above code is as follows,
# 
# Initialize num as 15
# 
# If the num >= 0
# 
# If num == 0 : num is zero
# 
# Else number has to be positive 
# 
# Else the number has to be negative

# In[3]:


#using ternory operator
num =15
print("Positive" if num>=0 else "Negative")


# ##### This method uses a ternary operator in Python to check whether a number is Positive or Negative.
# 
# For a user input num
# 
# Return “Positive” if num>=0 else “Negative”.
# Algorithm for the above code is as follows,
# 
# Initialize num as 15.
# print the output using ternary operator in python using print () function.

# In[4]:


#using if and elif  
num = 15
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')


# #### Algorithm for the above code is as follows,
# 
# Initialize num as 15
# 
# If the num > 0: it is a positive number.
# 
# If the num < 0: it is a Negative number.
# 
# Else the number has to be zero itself

# In[ ]:




