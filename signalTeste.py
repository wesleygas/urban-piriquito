
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
import sounddevice as sd


class signalMeu:

    def __init__(self):
        self.init = 0
        self.fs = 48000
        #sd.default.samplerate = self.fs
        #sd.default.channels = 1

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
    def geraNum(self, number, amplitude=1, duration = 1):
        listaFreq = [[941,1336], [697,1209],
                    [697,1336], [697,1477],
                    [770,1209], [770,1336],
                    [770,1477], [852,1209],
                    [852,1336], [852,1477] ]
        #print(listaFreq[number])
        time, sinal = self.generateSin(listaFreq[number][0],amplitude,duration,self.fs)
        time, sinal1 = self.generateSin(listaFreq[number][1],amplitude,duration,self.fs)
        sinalF = np.add(sinal, sinal1)/2
        
        return time,sinalF

    def geraSeq(self, numero, pressTime = 0.25, intervalTime = 0.05,):
        delay = np.zeros(int(intervalTime*self.fs))
        finalSignal = []
        for digit in range(len(numero)-1):
            tempo, signal = geraNum(int(numero[digit]), duration=pressTime)
            finalSignal.append(signal)
            finalSignal.append(delay)
        tempo, signal = geraNum(int(numero[-1]), duration=pressTime)
        finalSignal.append(signal)
        finalSignal = np.concatenate(finalSignal)
        
        return finalSignal
    def playSig(self, signal):
        sd.playrec(signal, self.fs, channels=1)