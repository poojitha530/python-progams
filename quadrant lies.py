#!/usr/bin/env python
# coding: utf-8

# In[3]:


# for initialization of coordinates
x, y = map(int, list(input("Insert the value for variable X and Y : ").split(" ")))
# find true condition of first quadrant
if x > 0 and y > 0:
    print("point (", x, ",", y, ") lies in the First quadrant")
# find second quadrant
elif x < 0 and y > 0:
    print("point (", x, ",", y, ") lies in the Second quadrant")
# To find third quadrant
elif x < 0 and y < 0: 
    print("point (", x, ",", y, ") lies in the Third quadrant")
# To find Fourth quadrant 
elif x > 0 and y < 0:
    print("point (", x, ",", y, ") lies in the Fourth quadrant")
# To find does not lie on origin
elif x == 0 and y == 0:
    print("point (", x, ",", y, ") lies at the origin")
# On x-axis
elif y == 0 and x != 0:
    print("point (", x, ",", y, ") on x-axis")
# On y-axis
elif x == 0 and y != 0:
    print("point (", x, ",", y, ") on at y-axis")


# ### Python program to find out the quadrant in which the given co-ordinate lie
# Working :
# According mathematics quadrants rules:
# 
# X  is positive integer as well as Y is also positive a integer it signifies first quadrant.
# 
# X  is negative integer but Y is positive integer it signifies second quadrant.
# 
# X  is negative integer as well as Y is also negative integer it signifies third quadrant.
# 
# X  is positive integer but Y is negative integer it signifies fourth quadrant.
# 
# Algorithm :
# 
# Get value of x & y
# 
# If ( x>0 and y>0 ) First Quadrant
# 
# If ( x<0 and y>0 ) Second Quadrant
# 
# If ( x<0 and y<0 ) Third Quadrant
# 
# If ( x>0 and y>0 ) Fourth Quadrant
# 
# If ( x=0 and y=0 ) Origin
# 
# If ( x!=0 and y=0 ) x-axis
# 
# If ( x>0 and y>0 ) y-axis

# 
