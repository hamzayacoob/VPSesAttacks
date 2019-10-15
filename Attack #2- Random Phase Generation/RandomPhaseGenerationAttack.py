#!/usr/bin/env python
# coding: utf-8

# In[285]:


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


# In[288]:


#Read in the amplitude of the audio file
fs, data = scipy.io.wavfile.read(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\AudioFiles\helloAudio.wav")
length = len(data)
print("This is the data printed\n", data[-100:])


# In[289]:


a = data

#Take the FFT of the time domain frequency 
b = sc.fft(a)

#Gets half of the spectrum, using ceil to obtain the middle value in case of an odd length
#Only need half of it because real and imaginary data are symmertrial and data duplicates after half way
c= b[0:int(np.ceil((length+1)/2.0))]

#Store new length of the array
lenFreq = len(c)

#Take the magnitude of the FFT for original audio
magFreq = np.absolute(c)


# In[290]:


print("This is magFreq:\n", magFreq)
print("\n", c)


# In[ ]:





# In[291]:


print(np.abs(4+3j))
print(c[:10])


# In[361]:


"""Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
def sum_to_n(n, size, limit=None):
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
            yield (np.sqrt([i] + tail))
            #list.append(np.sqrt([i] + tail))


# In[362]:


#Stores the original real and imaginary numbers in a list
realNumbers = []
imaginaryNumbers = []

#Stores the magnitudes for the pertubated audio clip
magFreq2 = []

#Stores the modified real and imaginary numbers in a list
realFinal = []
imagFinal = []

#Stores the results in the following lists 
resultsTemp = []
finalResults = []

for i in range(lenFreq-1):
    #Stores the result inside of real numbers list
    realNumbers.append(c[i].real)
    
    #Stores the numbers inside of imaginary numbers list
    imaginaryNumbers.append(c[i].imag)
    
    #Stores the magnitude inside of the list
    #Uses the abs function to be able to compute the magnitude
    valueToUseInSumN = np.abs(complex(c[i].imag*1j + c[i].real))
    magFreq2.append(np.power(valueToUseInSumN, 2))
    
    for x in sum_to_n(magFreq2[i]*.0001, 2):
        #add the result to a list
        resultsTemp.append(x)
        break
    
    finalResults.append(resultsTemp[0][0] + complex(resultsTemp[0][1])*1j)
    
    realFinal.append(finalResults[i].real * 100)
    imagFinal.append(finalResults[i].imag* 1j* 100)
    
    resultsTemp.clear()


# In[368]:


magFreq3 = []


# In[223]:


results = []


# In[224]:


for x in sum_to_n(magFreq2[1], 2):
    #add the result to a list
    results.append(x)
    #print(x)
    break


# In[346]:





# In[242]:


(results[0][0] + complex(results[0][1])*1j)


# In[296]:


(complex(c[i].imag*1j + c[i].real))


# In[369]:


someNum= np.abs(complex(c[1].imag*1j + c[1].real))


# In[370]:


someNum


# In[371]:


np.power(someNum, 2)


# In[372]:


magFreq3.append(np.power(someNum, 2))


# In[373]:


magFreq3


# In[374]:


magFreq2[1]


# In[375]:


resultsTemp11 = []
finalResults11 = []
for x in sum_to_n(magFreq3[0]*.0001, 2):
        #add the result to a list
        resultsTemp11.append(x)
        break
    
finalResults11.append(resultsTemp11[0][0] + complex(resultsTemp11[0][1])*1j)
    


# In[376]:


reals = []
fakes = []
reals.append(finalResults11[0].real * 100)
fakes.append(finalResults11[0].imag* 1j* 100)


# In[377]:


print(reals[0])
print(fakes[0])


# In[378]:


np.abs(reals[0]+fakes[0])


# In[204]:


type(results)


# In[338]:


finalResults11[0].imag


# In[275]:


testData = finalResults


# In[279]:


magFreq2


# In[280]:


np.abs(testData[0])


# In[281]:


testData


# In[ ]:





# In[333]:


1712700*np.sqrt(2)


# In[351]:


magFreq


# In[366]:


realFinal


# In[367]:


imagFinal


# In[ ]:




