#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.positive negative


# In[1]:


positive = ['good','awesome','best','nice']
negative = ['worst','awful']
comments = ['He is a good boy','Food is the worst here','He is an awesome player','She is the best','This pizza tastes awful','These burger are really nice']
p=[];n=[]
result =[]
for i in comments:
    for j in i.split():
        if j in positive:
            p.append(i)
        elif j in negative:
            n.append(i)
print("Positive Comments: ")
for j in p:
    print(' ',j) 
       
print("Negative Comments: ")
for j in n:
    print(' ',j)


# In[ ]:


#2.dictionary


# In[4]:


import numpy as np
import math
dict={'Square':lambda x: x**2 ,'Cube':lambda x: x**3 ,'Squareroot':lambda x:np.sqrt(x)}
num=int(input("enter the num: "))
result=0
for s in dict.keys():
   result += dict[s](num)
      
print(result)


# In[ ]:


#3fruits


# In[5]:


fruits = (('Lemon','sour'),('DragonFruit', 'Sweet'),('Grapes','sour'),('Kiwi','Sour'),('Apples', 'sweet'),('Orange', 'sour'),('Blueberries','sweet'),('Limes','Sour'))

s_Fruits=[]

for i in fruits:
    if(i[1].lower()=='sour'):
        s_Fruits.append(i[0])
 
print("Sour Fruits: ", s_Fruits)


# In[ ]:


#4list


# In[6]:


ls = ['hello','Dear','hOw','ARe','You']
result=[]
for i in ls:
    if(i[1].isupper()):
        result.append(i)
print(result)


# In[ ]:


#5 moon


# In[7]:


weight_on_moon = {'Jhon':45,'shelly':65,'Marry':35}

i = lambda x: round((x/9.81)*1.622, 2)
a = lambda k: (k, l(weight[k]))
la = dict(ans(x) for x in weight_on_moon)
print(la)


# In[ ]:


#8 cumulative avg


# In[13]:


a = [9,8,7,6,5]
import itertools as it
abc=[9,8,7,6,5]
abc = it.accumulate(a)
print(list(abc))


# In[9]:


#9 list


# In[10]:


lsbool = map(lambda x:x.upper(),["True","FALse","tRUe","tRue","False","faLse"])
upperlist=list(lsbool)
print(upperlist)


# In[11]:


#10 dob


# In[12]:


dateslist=['17-12-1997','22-04-2011','01-05-1993','19-02-2020']
year=[]
for j in dateslist:
    year.append(j[6:])
print(year)


# In[ ]:




