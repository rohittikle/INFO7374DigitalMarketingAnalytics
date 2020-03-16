#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import streamlit as st

# In[1]:


reward_list= [1231,1210,1480,1396,1209,1083,1160,1244,1190,874,654,1070,254,280,297,297,599,361,361,392,358,249,411,410,409,409,290,351,353,348,442,321,315,316,321,476,349,229,230,237]


# In[ ]:





# In[2]:


print(len(reward_list))


# In[5]:


pitch_list= [0.1,0.25,0.5,1.0,1.5,2.0,2.5,3.0]
#pitch = st.slider( 'pitch')
#st.write(pitch, 'The pitch value is in the range')


# In[6]:


print(len(pitch_list))


# In[7]:


lta_list=[]
fta_list=[]
usa_list=[]
la_list=[]
tda_list=[]
i = 0
while i < len(reward_list):

  lta_list.append(reward_list[i])
  fta_list.append(reward_list[i+1])
  usa_list.append(reward_list[i+2])
  la_list.append(reward_list[i+3])
  tda_list.append(reward_list[i+4])
  i = i+ 5


# In[12]:
#add_slider = st.sidebar.slider(
    #'Select a range of values',
  #  0.1, 3.0, (0.25, 1.25)
#)

import matplotlib.pyplot as plt 
#add_selectbox = st.sidebar.selectbox('Which attribution model would you like to choose',('LTA', 'FTA', 'USA', 'LA', 'TDA'))

a=[lta_list,fta_list,usa_list,la_list,tda_list]
b=['LTA','FTA','USA','LA','TDA']

variables = st.sidebar.multiselect("Select the variables. LTA- Last Touch Attribution, FTA - First Touch Attribution, TDA- Time Decay Attribution,USA- U Shaped Attribution, Linear Attribution -LA ", b)
#st.write("You selected these variables", variables)



for i, j in zip(a, variables):
  plt.plot(pitch_list, i,marker='o',label=j)

#plt.plot(pitch_list, fta_list,marker='o',label='FTA')
#plt.plot(pitch_list, usa_list,marker='o',label='USA')
plt.legend()
plt.show()
st.pyplot()

# In[ ]:




