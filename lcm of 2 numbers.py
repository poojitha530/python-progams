#!/usr/bin/env python
# coding: utf-8

# In[3]:


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


def lcm(a, b):
    return (a * b) // hcf(a, b)


first = int(input("enter first number:"))
second = int(input("enter second number:"))

print("Lcm of", first, "and", second, "is", lcm(first, second))


# In[ ]:




