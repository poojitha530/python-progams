#!/usr/bin/env python
# coding: utf-8

# #### palindrome number --> 
# The Numbers that when reversed is the same as the original number itself are known as Palindromic Numbers.
# 
# example : 121,4224,

# In[ ]:





# In[1]:


num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")


# In[ ]:




