#!/usr/bin/env python
# coding: utf-8

# In[6]:


val2 = [[['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'BKNO', '8438', 'BKNO', '', ''], ['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'PGNO', '581', 'PGNO', '', '']], 
        [['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'BKNO', '84812', 'BKNO', '', ''], ['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'PGNO', '581', 'PGNO', '', '']], 
        [['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'BKNO', '08438', 'BKNO', '', ''], ['input', '37179-20220409-01\\NCUNIO-2022_00011678', 'PGNO', '581', 'PGNO', '', '']]]


# In[10]:


for i in val2:
    k = i[0][3]
    print(k)
    vals = sorted(k, reverse=True)
    print(vals)


# In[13]:


k = [8438,84812,8433]
vals = sorted(k)
print(vals)


# In[ ]:





# In[ ]:




