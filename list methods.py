#!/usr/bin/env python
# coding: utf-8

# #### list-->list is a collection of mutiple data type vales
# 

# ### list methods
# append()-->to add an element end of the list 
# 
# clear()-->removing all elements in the list
# 
# copy()-->it copy the list
# 
# count()-->count the specific element in the list
# 
# extend()-->to add list to the another list
# 
# index()-->returns the index of the element
# 
# insert()-->add an element at specified index value
# 
# pop()-->removes and retuns the last element from the list or given index value
# 
# remove()-->revome an element from the list
# 
# reverse()-->reverse the elements in the list
# 
# sort()-->sort the list ascending order
# 
# min()-->returns the min elements in the list
# 
# max()-->return the max element in the list

# In[1]:


a=[] #creation of list
print(type(a)) #ptinting the type of a


# In[3]:


a=list((1,2,3,4,5)) #creation of list using list function
print(a)


# In[4]:


a=[1,2,3,4,5]
print(a)


# In[10]:


a=[1,2,3,4,5]
print(a)


# In[11]:


b


# In[13]:


b.append('e')#adds the element at end of the list


# In[14]:


b


# In[15]:


b.clear()# it clears the list that ,means it gives an empty list
b


# In[16]:





# In[17]:


a=[1,2,3,4,5]
print(a)


# In[18]:


a.copy()#it copy the elements of the list
a


# In[20]:


a.count(2)#it gives count of specific value present in the  list


# In[21]:


a.append(2)


# In[22]:


a.count(2)


# In[23]:





# In[24]:


a


# In[25]:


b=['a','b','c','d']
a.extend(b)# it is used to add a list of elements in the another list


# In[26]:


a


# In[27]:


a.index('a')#it will shows the index values of a element


# In[28]:


a.index(5)


# In[30]:


a.insert(2,'s')


# In[31]:


a


# In[33]:


a.pop()#this method removes the last item and return that item


# In[40]:


a.remove(2)#it will remove the specific value in the list


# In[41]:


a


# In[42]:


a.reverse()#reverse the list


# In[43]:


a


# In[2]:


k=[11,12,24,54,68,97,45,33,98,6]
k.sort()#elements in list are sorted in ascending order
k


# In[ ]:





# In[ ]:




