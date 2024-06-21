#!/usr/bin/env python
# coding: utf-8

# #### leap year program

# In[3]:


#using if else statement
year=2023
if(year %400==0)or (year%4==0 and year%100!=0):
    print(year,"leap year")
else:
    print(year,"not leap year")


# In[7]:


#using calender module
import calendar

year = int(input("Enter a year: "))

if calendar.isleap(year):
    print(year, " is a leap year")
else:
    print(year, "is not a leap year.")


# In[12]:


#using ternory operator
def is_leap(year):
    return(year%4==0 and year%100!=0)or(year%400==0)
year=int(input("enter a year:"))
print(f"{year},is leap year" if is_leap(year) else f"{year},is not leap year")


# In[ ]:




