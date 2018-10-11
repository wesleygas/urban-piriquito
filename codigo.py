from signalTeste import *
from interface import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils
import matplotlib
matplotlib.use('TkAgg')

sig = signalMeu()
fs = 48000
sd.default.samplerate = fs
sd.default.channels = 1

listaFreq = [[941,1336], [697,1209],
             [697,1336], [697,1477],
             [770,1209], [770,1336],
             [770,1477], [852,1209],
             [852,1336], [852,1477] ]

def geraNum(number, amplitude=1, duration = 1, fs=48000):
    #print(listaFreq[number])
    time, sinal = sig.generateSin(listaFreq[number][0],amplitude,duration,fs)
    time, sinal1 = sig.generateSin(listaFreq[number][1],amplitude,duration,fs)
    sinalF = np.add(sinal, sinal1)/2
    
    return time,sinalF

def transmissao(duracao = 2):
	tempo, sinalao = geraNum(number=numero(), duration=duracao)
	myrecording = sd.playrec(sinalao, fs, channels=1)
	sd.wait()
	plt.plot(sinalao[:1000])
	plt.title('Sinal do numero até 1000')
	plt.show()


duration = 2
myrecording = sd.rec(int(duration * fs))
sd.wait()

cache = myrecording[0:fs,0]
frequencias,FFArray = sig.calcFFT(cache, fs)
frequencias = frequencias[:5000]
FFArray = FFArray[:5000]
indexes = peakutils.indexes(FFArray, thres=0.5, min_dist=70)
print(indexes)
indexes2 = []
for i in range(len(indexes)):
	indexes2.append(round(indexes[i]+2))
	indexes2.append(round(indexes[i]+1))
	indexes2.append(round(indexes[i]))
	indexes2.append(round(indexes[i]-1))
	indexes2.append(round(indexes[i]-2))
print(indexes2)
print(listaFreq[0][0])
number = 10
for i in range(len(indexes2)):
	for j in range(len(listaFreq)):
		if indexes2[i] == listaFreq[j][0]:
			if indexes2[i] == listaFreq[j][1]:
				numero = j



print(number)
plt.plot(frequencias,FFArray)
plt.show()






