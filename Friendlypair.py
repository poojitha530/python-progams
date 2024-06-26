#!/usr/bin/env python
# coding: utf-8

# In[7]:


def printDivisors(n, factors) :
    i = 1
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1, number2 = 6,28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print(number1,number2,"Friendly pair")
  else:
    print(number1,number2,"Not a Friendly Pair")


# ### Friendly Pair Numbers
# The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.
# Example: 6,28
# 
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# 
# As the ratio of both the number match, they are considered as a friendly pair.

# In[ ]:




