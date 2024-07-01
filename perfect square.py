#!/usr/bin/env python
# coding: utf-8

# In[4]:


#A perfect square is a number that can be expressed as the product of an integer by itself or as the second exponent of an integer. For example, 25 is a perfect square because it is the product of integer 5 by itself, 5 × 5 = 25.


from math import sqrt


def isPerfectSquare(x):
    if x >= 0:
        sr = int(sqrt(x))
        return (sr * sr) == x
    return False


n = int(input("enter number to check perfect square or not:"))
if isPerfectSquare(n):
    print(n,"is perfect square")
else:
    print(n,"is not perfect square")


# In[ ]:





# In[ ]:




