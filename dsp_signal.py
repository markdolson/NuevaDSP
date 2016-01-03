import numpy as np
from IPython.display import Audio
import matplotlib.pyplot as plt

class Signal:

    def __init__(self, signal):
        """
        signal - a list of numbers indicating values in the signal
        """
        self.signal = np.matrix(signal)
        self.sample_rate = 8000.0
        
    def __str__(self):
        return str(self.signal)

    def __add__(self, other):
        return Signal(self.signal + other.signal)

    def __mul__(self, other):
        
        if len(self.signal) != len(other.signal):
            raise ValueErrror("Cannot multoply signals with different lengths")

        result = []
        for i in range(self.signal.size):
            result.append(self.signal[0,i]*other.signal[0,i])

        return Signal(result)

    
    def make_audio(self):
        return Audio(data=self.signal, rate=self.sample_rate)


def plot_signal(signal, add=False):
    x_axis_step = 1.0/signal.sample_rate
    time = x_axis_step * signal.signal.size
    x_axis = np.arange(0, time, x_axis_step)
    print(x_axis)
    plt.plot(x_axis, signal.signal.transpose())
    plt.xlabel("Seconds")
        
