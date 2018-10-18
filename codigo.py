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

def recepcao():
	duration = 2
	myrecording = sd.rec(int(duration * fs))
	sd.wait()
 
def analise(myrecording):
	cache = myrecording[0:fs,0]
	frequencias,FFArray = sig.calcFFT(cache, fs)
	frequencias = frequencias[:5000]
	FFArray = FFArray[:5000]
	indexes = peakutils.indexes(FFArray, thres=0.4, min_dist=50)
	print("indexes:   ", indexes)

	indexes2 = []
	p1num = []
	p2num = []
	for i in range(len(indexes)):
		indexes2.append(round(indexes[i]+2))
		indexes2.append(round(indexes[i]+1))
		indexes2.append(round(indexes[i]))
		indexes2.append(round(indexes[i]-1))
		indexes2.append(round(indexes[i]-2))
	print("indexes2:   ",indexes2)
	number = 10
	for i in range(len(indexes2)):
		for j in range(len(listaFreq)):
			if indexes2[i] == listaFreq[j][0]:
				p1num.append(j)
				print(p1num)
			if indexes2[i] == listaFreq[j][1]:
				p2num.append(j)
				print(p2num)
	for i in range(len(p1num)):
		for j in range(len(p2num)):
			if p1num[i] == p2num[j]:
				print(p1num[i], "e", p2num[j])
				number = p1num[i]
				print(number)
				break

	print(number)
	if number < 10:
		print(number)
		plt.plot(myrecording)
		plt.show()
		plt.plot(FFArray)
		plt.show()
	else:
		print("erro")
	
	

duration = 1
myrecording = sd.rec(int(duration * fs))
sd.wait()
while True:
	sd.wait()
	analise(myrecording)
	myrecording = sd.rec(int(duration * fs))






