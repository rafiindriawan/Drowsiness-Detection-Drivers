#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import shutil
import glob
from tqdm import tqdm


# In[3]:


Raw_DIR= 'D:\KULIAH\Skripsi\CV_Driver_Drowsiness_Detection\MRL Eye Data\mrlEyes_2018_01'
for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4]=='0':
            shutil.copy(src=dirpath+'/'+i, dst=r'D:\KULIAH\Skripsi\CV_Driver_Drowsiness_Detection\MRL Eye Data\Prepared_Data\Open Eyes')
            
        elif i.split('_')[4]=='1':
            shutil.copy(src=dirpath+'/'+i, dst=r'D:\KULIAH\Skripsi\CV_Driver_Drowsiness_Detection\MRL Eye Data\Prepared_Data\Close Eyes')
        


# In[ ]:




