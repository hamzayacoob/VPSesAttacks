#!/usr/bin/env python
# coding: utf-8

# In[4]:


import speech_recognition as sr
from os import path
import os.path
import operator
from os import system
from os import listdir
from os.path import isfile, join
import wave
import scipy as sc
import librosa
import IPython.display as ipd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import math
import librosa as lb
import scipy
from sklearn.decomposition import PCA
import pandas as pd
from os import listdir
from os.path import isfile, join
import time
from itertools import product
import datetime
import sys


# In[18]:


fs, data = scipy.io.wavfile.read(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\AudioFiles\helloAudio.wav")
print(len(data))


# In[19]:


h = [3, 4]
print(h)


# In[20]:


#Squares both the phase signals and adds them together
def getSignalSum(a, b):
    x = (a**2) + (b**2)
    return x


# In[21]:


#Obtains the magnitude of the signalSums
def getMagnitude(x):
    ans = math.sqrt(x)
    return ans


# In[93]:


print("This is the signal sum: ",getSignalSum(3,4))
signalSum = getSignalSum(3,4)
print(np.power(np.abs(3+4j), 2))
print("This is the magnitude of the signal: ",getMagnitude(signalSum))
magnitude = getMagnitude(signalSum)


# In[ ]:





# In[94]:


#Sets the upper bound on possible value that a signal can be
def signalBound(y):
    maxNum = np.sqrt(y)
    return maxNum
    


# In[95]:


maxNum = signalBound(signalSum)
print("This is the highest value that a new\nsignal number can be to have the same magnitude:\n",maxNum)


# In[96]:


def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        #list.append([n])
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in np.arange(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield np.sqrt([i] + tail)
            #list.append(np.sqrt([i] + tail))


# In[113]:


#Create a new empty list to store the answers
listAns = []
result = []


# In[114]:


for x in sum_to_n(np.power(np.abs(-2.42218600e+06+1.22079065e-12j)*.0001, 2), 2):
    #add the result to a list
    result.append(x)
    #print(x)
    break


# In[115]:


print(result)
print(type(result))


# In[107]:


data = np.asarray(result)
print(data)


# In[ ]:





# In[79]:


################   TEST CODE      ###############33


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




