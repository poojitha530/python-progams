#!/usr/bin/env python
# coding: utf-8

# In[7]:


#An Armstrong number or a Narcissistic number is any number that sums up itself when each of its digits is raised to the
#power of a total number of digits in the number. 
low=int(input("enter low range:"))
high=int(input("enter high range value"))
for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")


# In[ ]:




