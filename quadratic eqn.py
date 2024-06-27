#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a program to find roots of a quadratic equation in Python
import math
 
def findRoots(a, b, c):
 
    if a == 0:
        print("Invalid")
        return -1
        
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
 
    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2*a))
    else:  # d<0
        print("Roots are complex")
        print(- b / (2*a), " + i", sqrt_val)
        print(- b / (2*a), " - i", sqrt_val)
# Driver Program
a = 1
b = 4
c = 4
# Function call
findRoots(a, b, c)


# ###  find the roots of quadratic equation
# Mainly roots of the quadratic equation are represented by parabola in 3 different patterns like
# 
# No Real Roots
# 
# One Real Root
# 
# Two Real Roots
# 
# When we solve the equation we get 3 conditions mentioned above using this formula:-
# 
# X = [-b (+or-) [sqrt(pow(b,2)-4ac)] ] / 2a
# 
#  
# 
# Algorithm :
# 
# Calculate Discriminant (D)
# 
# D = b^2 – 4*a*c
# 
# If D>0 : Two real root exists.
# 
# If D=0 : Equal root exists.
# 
# If D<0 : Imaginary root exists.

# In[ ]:




