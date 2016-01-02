import numpy as np

class Signal:

    def __init__(self, signal):
        """
        signal - a list of numbers indicating values in the signal
        """
        self.signal = np.matrix(signal)
        self.sample_rate = 8000.0
        
    def __add__(self, other):
        return Signal(self.signal + other.signal)

    def __mul__(self, other):
        
        if len(self.signal) != len(other.signal):
            raise ValueErrror("Cannot multoply signals with different lengths")

        result = []
        for i in range(self.signal.size):
            result.append(self.signal[0,i]*other.signal[0,i])

        return Signal(result)

    
