#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def transcribe(my_path,model):
    wit_key = ''

    AUDIO_FILE =  path.join(my_path)

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(my_path) as source:
        audio = r.record(source)  # read the entire audio file

    if(model == 'google'):
        # Google
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
             print("Google: -_-")
            
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
    


# In[6]:


fs, data = scipy.io.wavfile.read(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\venmo.wav")
elementsInBucket = 25
n = int(len(data)/elementsInBucket)

#Breaks array into buckets of elements
def createBuckets(arr, n):
    length = len(arr)
    return [ arr[i*length // n: (i+1)*length // n] 
             for i in range(n) ]

#Load audio file
arr = np.copy(data)
#Store split array into variable
splitArray = createBuckets(arr,n)

l = list()

for x in splitArray[:n]:
    #print(np.fliplr([x])[0])
    l.extend(np.fliplr([x])[0])

data2 = np.asanyarray(l)

scipy.io.wavfile.write(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\venmo_temp.wav", fs, data2)
transcribe(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\venmo_temp.wav", "google")


# In[ ]:




