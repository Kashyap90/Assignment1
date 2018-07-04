
# coding: utf-8

# In[1]:


int=[]
for i in range(2000, 3201):
    if(i%7==0) and (i%5!=0):
        int.append(str(i))
        print(','.join(int))

