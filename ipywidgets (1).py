#!/usr/bin/env python
# coding: utf-8

# In[19]:


import ipywidgets as w # importing ipywidgets lib as w
a=len(dir(w)) #using len() method and dir() method 
print(a)
dir(w)


# In[20]:


def h(a,b): # definig h function
    return a+b# return values
w.interact(h,a=10,b=30) #calling function


# In[21]:


def k(l,p):# definig  function
    return l
    return p
w.interactive(k,l=True,p=30) #calling function using interactive method


# In[22]:


def k(l,p):# definig  function
    return l
    return p
w.interact(k,l=True,p=30)#calling function using interact method


# In[23]:


def k(s):# definig  function
    return s
w.interact(k,s=[1,2,3,4,5])#calling function using interact method


# In[24]:


def z(s):#defining function using def keyword
    for i in range(s):
        print(i)
w.interact(z,s=10)#calling function using interact method


# In[25]:


def f(K):
    return x*12


# In[26]:


p=w.BoundedFloatText() #assinging boundedFloatText to the p variable
q=w.FloatText()#assing FloatTest to the q varialble
def h(): #define function
    return (p.value,q.value) #returnin p,q values
def inter(self): #defining inter function using def keyword and its takes self 
    w.interact(h);#calling interact method
b=w.Button(description='click me') #assing button 
display(p) #displays the p
display(q)#displays q
display(b)#displays button
b.on_click(inter)# calling the inter  function using b object


# In[27]:


slider1=w.IntSlider()# slider1 takes the int value
slider2=w.IntSlider()# slider2 takes the int value
display(slider1)#displays the slider1 value
display(slider2)#displays the slider2 value
def out_put():# defining the out_put function
    print(slider1.value)#printing the value of slider1
    print(slider2.value)#printing the value of slider2
w.interact(out_put)#calling the interact method
    


# In[28]:


slider1=w.IntSlider()
slider2=w.IntSlider()
display(slider1)
display(slider2)
def out_put():
    print(slider1.value)
    print(slider2.value)
w.interact(out_put,slider1=slider1.value,slider2=slider2.value)
    


# In[29]:


slider1=w.FloatSlider()#it takes float value
slider2=w.FloatSlider()#it takes float value
display(slider1)#displays slider1 value
display(slider2)#displays slider2 value
def out_put():# defining the out_put function
    return slider1.value #returning the slider1 value
    return slider2.value#returning the slider2 value
w.interact(out_put)#calling the interact method
    


# In[30]:


def f(x,y):#defineing f function and it takes arguments x,y
    return x+y #returning the sum of x ,y
g=w.interact(f,x=10,y=20) #callig the interact method and giving x value 10 and y value 20


# In[31]:


slider1=w.IntSlider()# slider1 takes the int value
slider2=w.IntSlider()# slider2 takes the int value
display(slider1)#displays the slider1 value
display(slider2)#displays the slider2 value
def out_put():#defining the function named out_put
    print(slider1.value+slider2.value)#printing the sum of slider 1,slider2
def execution(self):#creating execution function
    w.interact(out_put)#calling  interact method
button=w.Button(description="click me")
button.on_click(execution)
display(button)


# In[32]:


import ipywidgets as w
a1=w.IntSlider()
b1=w.IntSlider()
j=w.Button(description="submit:")
j1=w.Text(description="value:")
display(w.VBox([a1,b1,j,j1]))
def add():
    j1.value=str(a1.value+b1.value)
def display1(self):
    w.interact(add)
j.on_click(display1)


# In[33]:


import ipywidgets as w
a1=w.IntSlider(value=20,min=10,max=100,step=5)
b1=w.IntSlider()
j=w.Button(discription="submit")
j1=w.Text(discription="value:")
display(w.VBox([a1,b1,j,j1]))
def add():
    j1.value=str(a1.value+b1.value)
def display1(self):
    w.interact(add)
j.on_click(display1)


# In[34]:


a=w.IntSlider()# a takes the int value
j=w.Button(description="submit")# it is a submit button 
j1=w.Text(description="value:")#it is a text value bar
def prime(n): #defining a prime function using def keyword and it takes one parameter n
    f=True #f is assined as true value
    if n<2: # if condition ,in this checking n value is lessthan 2 or not
        f=False # n value <2---> f is false that means its is < 2 it is not prime number
        for i in range(2,n): #for loop -->i is in range of 2 and n 
            if n%i==0:
                f=False
                break
                if f:
                    j1.value=str(n)+"is prime number"
                else:
                    j1.value=str(n)+"is not prime number"
    def display1(change):
        prime(a.value)
    j.on_click(display1)
display(w.VBox([a,j,j1]))


# In[35]:


import ipywidgets as w
def h(b):
    for i in range(2,b):
        if b%i==0:
            print("not prime",b)
            break
        else:
            print("prime number",b)
            break
kk=w.interact(h,b=7)


# In[ ]:





# In[36]:


import ipywidgets as w
a1=w.HTML("<H1>Applications Form</H1>")
b1=w.Text(description="Name:")
c1=w.DatePicker(description ="Date of Birth")
d1=w.RadioButtons(description="Gender",options=["male","female"])
e1=w.Text(description="F.N:",value="Name")
f1=w.Text(description="school")
g1=w.Textarea(description="address")
h1=w.Button(description="submit")
h3=w.Textarea(description="values")
display(w.VBox([a1,b1,c1,d1,e1,f1,g1,h1,h3]))
def prt():
    h3.values=("{},{},{},{},{},{}".format(b1.value,c1.value,d1.value,d1.value,e1.value,(f1.value),(g1.value)))
def send(self):
    w.interact(prt)
h1.on_click(send)


# In[37]:


import ipywidgets as w
name=w.Text(description="name:",padding=4)
color=w.Dropdown(description="color:",padding=4,options=['red','orenge','yellow','green','blue'])
page1=w.Box(chlidren=[name,color],padding=4)
age=w.IntSlider(description="Age",padding=4,min=0,max=120,value=25)
gender=w.RadioButtons(description="Gender:",padding=4,options=['male','female'])
page2=w.Box(children=[age,gender],padding=4)
tabs=w.Tab(children=[page1,page2])
hn=w.Textarea(description="value")
display(tabs)
tabs.set_title(0,'Name')
tabs.set_title(1,'Details')
pri=0
def g():
    global pri
    pri=pri+1
    s=(str(pri)+".Name:"+name.value)
    h=("Age :"+str(age.value))
    k=("color :"+str(color.value))
    j=("gender:"+str(gender.value))
    hn.value="{},{},{},{}".format(s,h,k,j)
display(button)
def u(self):
    w.interact(g)
button.on_click(u)
display(hn)


# ### calculator

# In[38]:


exec("print(5+6)")


# In[39]:


print(5+6)


# In[40]:


def test():
    print("function working")


# In[41]:


test()


# In[42]:


exec("test()")


# In[43]:


import ipywidgets as w 


# In[44]:


h=w.Text(description="enter operation")
display(h)


# In[51]:


import ipywidgets as w
h=w.Text(description="enter operation")
button=w.Button(description="click me")
def operation():
    g="print({})".format(h.value)
    exec(g)
def execute(self):
    w.interact(operation)
button.on_click(execute)
display(h)
display(button)


# In[52]:


import ipywidgets as w
h=w.Text(description="enter operation")
button=w.Button(description="click me")
def operation():
    exec("print({})".format(h.value))
def execute(self):
    w.interact(operation)
button.on_click(execute)
display(h)
display(button)


# In[ ]:




