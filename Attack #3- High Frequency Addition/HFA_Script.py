#!/usr/bin/env python
# coding: utf-8

# In[13]:


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


# In[16]:


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


# In[20]:


def HFA(path, frequency, intensity):
    fs, data = scipy.io.wavfile.read(path)
    print(len(data))
    length = len(data)
    
    #2. Generates a high frequency sin wave
    #Allows the sine wave to be broadcastable to the audio file we are testing
    sampleRate = fs #give it the same sample rate as the original audio
    frequency = frequency
    duration = length/sampleRate #how long the audio sound is in seconds  #4.52

    t = np.linspace(0, duration, sampleRate * duration)  #  Produces a 'duration' long Audio-File in seconds
    y = np.sin(frequency * 2 * np.pi * t) * (intensity)  #Use to control the intensity of the sin wave

    #scipy.io.wavfile.write(path[0:-4]+''+'_SINEwav_Frequency'+''+str(fs)+'_Intensity'+str(intensity)+'.wav', sampleRate, y)
    #plt.plot(y)
    #print("This is the length of the sin sound wave:",len(y))

    #3. Merges the sine wave high frequency with the original piece of audio
    resultSound = np.add(data[:length-1] , y[:length] )

    #4. Casts the result sound from a float to an int
    resultSound = np.asarray(resultSound,dtype=np.int16)
    #print(resultSound)

    #5. Writes the audio file and then transcribes it 
    scipy.io.wavfile.write(path[0:-4]+''+'_OutputWav_Frequency'+''+str(fs)+'_Intensity'+str(intensity)+'.wav', sampleRate, resultSound)
    transcribe(path[0:-4]+''+'_OutputWav_Frequency'+''+str(fs)+'_Intensity'+str(intensity)+'.wav', "google")

