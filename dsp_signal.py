import numpy as np
from IPython.display import Audio
import matplotlib.pyplot as plt
import random, wave, math
import scipy.signal, scipy.io.wavfile

DEFAULT_SAMPLE_RATE = 10000.0

class Signal:

    def __init__(self, signal):
        """
        signal - a list of numbers indicating values in the signal
        """
        self.signal = np.matrix(signal)
        self.sample_rate = DEFAULT_SAMPLE_RATE
        
    def __str__(self):
        return str(self.signal)

    def __add__(self, other):
        if isinstance(other, Signal):
            return Signal(self.signal + other.signal)
        
        return Signal(np.add(self.signal, other))

    def __mul__(self, other):
        
        if not isinstance(other, Signal):
            return Signal(np.multiply(self.signal, other))

        if len(self.signal) != len(other.signal):
            raise ValueErrror("Cannot multiply signals with different lengths")

        result = []
        for i in range(self.signal.size):
            result.append(self.signal[0,i]*other.signal[0,i])

        return Signal(result)

    
    def make_audio(self):
        return Audio(data=self.signal, rate=self.sample_rate)


    def plot_signal(self):
        x_axis = np.linspace(0, time, num=self.signal.size)
        plt.plot(x_axis, self.signal.transpose())
        plt.xlabel("Seconds")
        

    def shift(self, amount):
        new_sig = []
        if amount >= 0:
            for i in range(amount):
                new_sig.append(0)
            for i in range(self.signal.size-amount):
                new_sig.append(self.signal[0, i])
        else:
            for i in range(amount*-1, self.signal.size):
                new_sig.append(self.signal[0, i])
            for i in range(amount*-1):
                new_sig.append(0)

        return Signal(np.matrix(new_sig))

    def stretch(self, amount):
        samples = amount * self.signal.size
        new_sig = scipy.signal.resample(self.signal, samples, axis=1)
        return Signal(np.matrix(new_sig))

    def clip(self, start, end):
        return Signal(self.signal[:, start:end])

    def concatenate(self, other):
        return Signal(np.concatenate([self.signal, other.signal], 1))

def make_uniform_random_signal(length, minimum=-32768, maximum=32768):
    signal = []
    for i in range(length):
        signal.append((random.random() * (maximum-minimum)) + minimum)

    return Signal(signal)

def make_gaussian_random_signal(length, mean=0, sd=1000):
    signal = []
    for i in range(length):
        signal.append(np.random.normal())

    return Signal(signal)
    

def make_signal_from_wav(filename, channel=0):
    
    rate, data = scipy.io.wavfile.read(filename)
    data = data.T #convert to row matrix

    if channel >= data.shape[0]:
        print("Warning: Channel " + str(channel) + " requested but only " + \
              str(data.shape[0]-1) + " channels present. Defaulting to 0")
        channel = 0

    data = data[channel, :]
    data = np.asmatrix(data)
    seconds = data.size/rate
    samples = DEFAULT_SAMPLE_RATE * seconds

    resampled = scipy.signal.resample(data, samples, axis=1)
    return Signal(resampled)

def make_sin_signal(frequency, phase_shift, length):
    cycles = float(length)/(DEFAULT_SAMPLE_RATE*frequency)
    phase_shift = phase_shift % (2*math.pi)
    cyc = np.linspace(phase_shift, phase_shift+(2*math.pi), num=(length/cycles))
    
    signal = cyc
    for i in range(math.floor(cycles-1)):
        signal = np.concatenate([signal, cyc])

    #remainder = 
    return Signal(np.sin(signal))
    


