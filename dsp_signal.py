import numpy as np
from IPython.display import Audio
import matplotlib.pyplot as plt
import random
import scipy.signal

class Signal:

    def __init__(self, signal):
        """
        signal - a list of numbers indicating values in the signal
        """
        self.signal = np.matrix(signal)
        self.sample_rate = 10000.0
        
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
            raise ValueErrror("Cannot multoply signals with different lengths")

        result = []
        for i in range(self.signal.size):
            result.append(self.signal[0,i]*other.signal[0,i])

        return Signal(result)

    
    def make_audio(self):
        return Audio(data=self.signal, rate=self.sample_rate)


    def plot_signal(self):
        x_axis_step = 1.0/self.sample_rate
        time = x_axis_step * self.signal.size
        x_axis = np.arange(0, time, x_axis_step)
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

        self.signal = np.matrix(new_sig)

    def stretch(self, amount):
        samples = amount * self.signal.size
        new_sig = scipy.signal.resample(self.signal, samples, axis=1)
        self.signal = np.matrix(new_sig)

def make_random_signal(length):
    pass

def make_signal_from_wav(filename):
    pass

def make_sin_signal(f, theta, length):
    pass


