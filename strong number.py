#!/usr/bin/env python
# coding: utf-8

# ### strong number
# A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.
# Example: 145
# 
# Explanation : Number = 145
# 
# 145 = 1! + 4! + 5!
# 
# 145 = 1 + 24 + 120

# In[5]:


n =int(input("enter number to check strong or not"))
temp=n
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10): 
    f[i]=f[i-1]*i

while(temp):
    r=temp%10 
    temp=temp//10
    sum+=f[r] 

if(sum==n):
    print("Yes", n ,"is strong number")

else:
    print("No" , n, "is not a strong number")


# ### DOCUMENTATION FOR THIS CODE
# initally we take the  integer input as the number, we perform the following
# 
# Create a List of all the factorial values from 1 to 9.
# 
# Run a While loop until temp == 0.
# 
# Extract the Last Digit using Modulo Operator.
# 
# Shorten the length of the temp using divide operator.
# 
# Append the factorial of the digit in sum variable.
# 
# Check if the Sum matches the original string.

# 
