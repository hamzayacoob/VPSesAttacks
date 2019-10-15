#!/usr/bin/env python
# coding: utf-8

# In[50]:


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
import librosa.display
import contextlib


# In[74]:


#Read in the amplitude of the audio file
fs, data = scipy.io.wavfile.read(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\AudioFiles\helloAudio.wav")


# In[ ]:





# In[75]:


transcribe(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\AudioFiles\helloAudio.wav", "google")


# In[76]:


len(data)


# In[77]:


zeros = [0] * 100000


# In[78]:


new = data


# In[79]:


new = np.append(data, zeros)
new = np.asarray(new,dtype=np.int16)


# In[80]:


scipy.io.wavfile.write(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\attack4.wav", fs, new)


# In[81]:


transcribe(r"C:\Users\hamza\OneDrive\Desktop\ResearchML\attack4.wav", "google")


# In[24]:


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
    


# In[12]:





# In[ ]:





# In[ ]:




