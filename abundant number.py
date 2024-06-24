#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input("enter a number to check abundant number or not:"))

sum=1 # 1 can divide any number 

for i in range(2,n):
  if(n%i==0):    #if number is divisible by i add the number 
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')


# #### Abundant Number
# A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.
# 
# Example
# Number = 12
# 
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# 
# Now the sum of the factors except the number itself is :
# 
# 1 + 2 + 3 + 4 + 6 = 16
# 
# as the number 16>12 , the number itself.
# 
# It's an abundant number.

# In[ ]:




