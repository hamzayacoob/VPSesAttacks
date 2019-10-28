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
%matplotlib inline
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

def scramble_fft(ok_frame):
    ok_fft = np.abs(lb.audio.fft.fft(ok_frame))[0:int(len(ok_frame)/2+1)]
    
    new_ok = np.zeros_like(lb.audio.fft.fft(ok_frame))[0:int(len(ok_frame)/2+1)]
    
    i = 0
    while(True):
    #     print("index ",i)
        if(i>=ok_fft.shape[0]):
            break
        ok_fft_val = ok_fft[i]
        new_ok_val = findExample(ok_fft_val)
        if(np.equal(np.abs(new_ok_val),ok_fft[i])):
            new_ok[i] = new_ok_val
            i += 1
        else:
            continue

    new_ok_long = half_to_full(new_ok)
    new_ok_long = sc.ifft(new_ok_long)
    new_ok_long = throw_imaginary(new_ok_long)
    return new_ok_long

            
def throw_imaginary(fft_arr):
    result = np.zeros(len(fft_arr))
    for i in range(fft_arr.shape[0]):
        result[i] = fft_arr[i].real
    return result


def half_to_full(new):
    new_1 = new
    new_2 = np.delete(new_1, len(new_1)-1)
    new_2 = np.delete(new_2, 0)

    new_flp = np.append(new_1,np.flip(new_2,0))
    #     print(new_flp.shape)
    for i in range(1,int(len(new_flp)/2)):

        index_read = int(len(new_flp)/2-i)
        index_write = int(len(new_flp)/2+i)
    #     print("read ",index_read)
    #     print("write ",index_write)

        real = new_flp[index_read].real
        imag = new_flp[index_read].imag
    #     print("before",new_flp[index_write])
        new_flp[index_write] = real-imag*1j
    #     print("after",new_flp[index_write])
    return new_flp

            
def findExample(ok_fft_val):
    phase_angle = np.random.rand()*2
    phase_radians = math.pi*phase_angle
    real_part = math.sin(phase_radians)*ok_fft_val
    imag_part = math.cos(phase_radians)*ok_fft_val
    assert((real_part*real_part + imag_part*imag_part)**0.5-ok_fft_val < .0001)
    result = (real_part + imag_part*1j)
    radian_list[int(phase_angle*25/2)] += 1
    return result


def createBuckets(arr, n):
        length = len(arr)
        return [ arr[i*length // n: (i+1)*length // n] 
                 for i in range(n) ]
    

def output_RPG_Attack(attack, inputPath, outputPath, windowSize):
    ### Main Class ###
    radian_list = [0]*25
    #Read in the amplitude of the audio file
    fs, data = scipy.io.wavfile.read(inputPath)

    windowSize = windowSize
    n = int(len(data)/windowSize)

    arr = np.copy(data)

    #Store split array into variable
    splitArray = createBuckets(arr,n)

    l = list()

    for x in splitArray[:n]:
        l.extend(scramble_fft(x))


    data2 = np.asanyarray(l)
    data2= np.asarray(data2,dtype=np.int16)

    scipy.io.wavfile.write(outputPath, fs, data2)
    
    print("\nOriginal Audio Transcription:")
    print(transcribe(inputPath, "google"))
    print("\nPerturbed Audio Transcription:")
    print(transcribe(outputPath, "google"))

#Fill in the parameters for output_RPG_Attack and you are set!
#output_RPG_Attack()