#!/usr/bin/env python
# coding: utf-8

# ### calculator using ipywidgets

# In[7]:


import ipywidgets as w
h=w.Text(description="enter operation")
button=w.Button(description="click me")
clear_button=w.Button(description ="Reset")
op=w.Text(description="output")
H_box=w.HBox([h,button])



box=w.VBox([H_box,op,clear_button])
tab=w.Tab([box])
tab.set_title(0,"calculator")
def operation():
    g=eval("{}".format(h.value))
    op.value=str(g)
def execute(self):
    w.interact(operation)
def clear(self):
    h.value=""
    op.value=""
button.on_click(execute)
clear_button.on_click(clear)
display(tab)


# In[ ]:




