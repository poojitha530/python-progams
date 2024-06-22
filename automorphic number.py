#!/usr/bin/env python
# coding: utf-8

# #### AUTOMORPHIC NUMBER 
# Example
# 
# Input : number = 5
# 
# Output : It's an Automorphic number.
# 
# Explanation : Number = 5
# 
# Square of number = 25
# 
# as the square of the number ends with the number itself, It's an Automorphic number.

# In[4]:


number = 376
square = pow(number, 2)
mod = pow(10, len(str(number)))

# 141376 % 1000
if square % mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")


# ### Using Modulo Operators
#     in this method modulo operator to extract the last number of digits based on the length of the number input. We’ll reverse the number to match with the original numeric order of the digits.
# 
# Given an integer input as the number, we perform the following operations,
# 
# Find the square of the given integer input.
# 
# Check is the square % 10 ** len( str( number ) ) matches the original number itself.

# In[1]:


number = 376
square = pow(number, 2)
mod = pow(10, len(str(number)))

# 141376 % 1000
if square % mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")


# ### Using Endswith() Method
# The endswith() method returns True if the string ends with the specified value, otherwise False.

# In[5]:


# One line method for automorphic number in python
n = 376
# n^2 = 141376 141376[-3::] = 376
print("YES" if int(str(n**2)[-len(str(n))::]) == n else "No")


# In[ ]:




