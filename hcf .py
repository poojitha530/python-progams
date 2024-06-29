#!/usr/bin/env python
# coding: utf-8

# ### HCF of two numbers
# HCF means (Highest Common Factor) also known as GCD (Greatest Common Divisor).
# 
# x is called HCF of a & b two conditions :
# 
# x can completely divide both a & b leaving remainder 0
# 
# No, other number greater than x can completely divide both a & b

# In[7]:


num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
hcf=1
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        hcf=i
print("hcf of " ,num1 ,"and" ,num2, "is",hcf)


# In[ ]:




