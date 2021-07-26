#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[8]:


#ploting by specifying one axis only(By default it is considered as y axis coordinates)
# x axis default start from 0 and it takes same size for X as that of y axis i.e Here it is 5
plt.plot([1,2,3,4,5])


# In[10]:


# internally matplot use arrays 
arr=np.arange(0,5,0.2) #gap of 200ms
plt.plot(arr,arr,'r-')


# In[11]:


plt.plot(arr,arr,'b*')


# In[12]:


plt.plot(arr,arr,'r-',arr,arr*2,'bs',arr,arr*3,'g^')


# In[34]:


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9,3))
plt.subplot(221)
plt.bar(names,values)
'''The subplot call specifies numrows, numcols, plot_number where plot_number ranges from 1 to numrows*numcols.'''
plt.subplot(222)
plt.scatter(names,values)
plt.subplot(223)
plt.plot(names,values,'g-')
plt.suptitle('catagorial values plot')


# In[29]:


x=np.arange(0,5,1)
y=np.sin(x)
plt.plot(x,y)


# In[30]:


#setp can be used to set the properties of line
#plot function returns multiple line objects depending upon the lines it is ploting
line1,=plt.plot(np.arange(0,5,1),y)
plt.setp(line1,linewidth=2.0,color='r')
plt.xlabel('value')
plt.ylabel('sinx')


# In[37]:


'''You can create multiple figures by using multiple figure calls with an increasing figure number.'''
plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,4,],'r--')
plt.subplot(212)
plt.plot([3,4,5,6],'b-')
plt.figure(2)
plt.subplot(221)
plt.plot([1,2,3,4,],'g--')
plt.subplot(222)
plt.plot([1,2,3,4,],'y--')
plt.suptitle('Easy as 1, 2, 3')


# In[38]:


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
'''text can be used to add text in an arbitrary location,
and xlabel, ylabel and title are used to add text in the indicated locations'''

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# In[46]:


t=np.arange(0,5.0,0.1)
s=np.cos(2*np.pi*t)
line,=plt.plot(t,s,lw=2)
plt.annotate('local plot',xytext=(3,1.5),xy=(2,1),arrowprops=dict(facecolor='black', shrink=0.05))
plt.ylim(-2, 2)
plt.show()


# In[49]:


# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
# plot with various axes scales
plt.figure()

#subplots
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)

plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()


# In[ ]:




