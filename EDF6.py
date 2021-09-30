# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:53:45 2021

@author: Zikantika
"""
from PyEDF import EDFReader
from scipy import signal
import matplotlib.pyplot as plt
from copy import deepcopy
from math import ceil, floor
from struct import pack, unpack
import calendar
import datetime
import numpy as np
import os
import re
import warnings

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


file_in = EDFReader()
file_in.open('EEG-1.edf')

###reading from channels
####channel Zero

numSamples=256

print (file_in.readSamples(0, 0, 0))
print (file_in.readSamples(0, 0, 128))
#

t=file_in.readSamples(0, 0, 5000)

print(t.shape)
print(t.size)



#print(t.describe())

plt.plot(t)
plt.title("EEG Signal")
plt.xlabel('t (sec)')
plt.show()

signalnames=file_in.getSignalTextLabels()
print(file_in.getSignalTextLabels())

signalFrequecies=file_in.getSignalFreqs()

print(signalFrequecies)


FileHeader=file_in.readHeader()
print(FileHeader[0])

info=FileHeader[0];
numChannels=info['nchan']

print('number of Channels are')
print(numChannels)

channelsInfo=FileHeader[1]
print(channelsInfo)
#FileHeader['nchan']

numSamples=channelsInfo['n_samps']

numSample1=numSamples[0]

print(numSample1)



#file_in = EDFReader()
#file_in.open('EMG Artefact 1.edf')
#
#file_out = EDFWriter()
#file_out.open('EMG Artefact 2.edf')

header = file_in.readHeader()

#file_out.writeHeader(header)

meas_info = header[0]

print('Header File info')
print(meas_info)


for i in range(meas_info['n_records']):
    data = file_in.readBlock(i)
#    file_out.writeBlock(data)


t1=file_in.readSamples(1, 0, 10000)

print(t1.shape)
print(t1.size)



#print(t.describe())

plt.plot(t1)
plt.title("EEG Signal  Channel2" )
plt.xlabel('t (sec)')
plt.show()


sig=t1
sos = signal.butter(0, 4, 'lp', fs=1000, output='sos')
filtered = signal.sosfilt(sos, sig)


plt.plot(filtered)
plt.title('Delta Signal')
plt.xlabel('Time [seconds]')
plt.tight_layout()
plt.show()


Delta=filtered

sos = signal.butter(4, 8, 'lp', fs=1000, output='sos')
Theta = signal.sosfilt(sos, sig)


plt.plot(Theta)
#plt.set_title('Theta Signal')
#plt.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()



sos = signal.butter(30, 45, 'lp', fs=1000, output='sos')
Gamma = signal.sosfilt(sos, sig)


plt.plot(Gamma)
#plt.set_title('Gamma Signal')
#plt.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()

fs=256

x=Gamma

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

