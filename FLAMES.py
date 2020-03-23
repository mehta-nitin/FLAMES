#!/usr/bin/env python
# coding: utf-8

# ## FLAMES

# In[ ]:


def algo(fname,sname):       
    a = list(fname)
    b = list(sname)
    for i in a:
        for n in b:
            if i == n:
                a.remove(i)
                b.remove(n)
                count=0
            else:
                count=0

    return a+b

fname = input("Enter first name - ")
sname = input("Enter second name - ")
fname = fname.lower()
sname = sname.lower()
m = algo(fname,sname)
flames = ['F - Friend','L - Love','A - Affection','M - Marriage','E - Enemy']
count=0
n=4
while len(flames)!=1:
    for i in range(0,len(m)):
        if count<n:
            count+=1
        else:
            count=0
    flames.remove(flames[count-1])
    if count-1>-1:
        count-=1
    else:
        count=0
    n=n-1
print(flames)

