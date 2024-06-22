#!/usr/bin/env python
# coding: utf-8

# ### Harshad Number
# A Number that is divisible by the sum of it's digits is known as a Harshad number.
# 
# Input : 21
# 
# Output : Yes ' It's a Harshad Number.
# 
# Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.

# In[5]:


n = int(input("enter a number "))
p=n
l=[]
sum1=0
while(n>0):
    x=n%10
    l.append(x)
    n=n//10
sum1=sum(l)
if(p%sum1==0):
    print("Harshad number")
else:
    print("Not harshad number")


# In[ ]:





# In[ ]:




