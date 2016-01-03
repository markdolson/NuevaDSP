import dsp_signal

def test_addition():
    a = dsp_signal.Signal([1,2,3])
    b = dsp_signal.Signal([4,1,2])

    sum_signal = a + b
    assert(sum_signal.signal[0, 0] == 5)
    assert(sum_signal.signal[0, 1] == 3)
    assert(sum_signal.signal[0, 2] == 5)

def test_mult():
    a = dsp_signal.Signal([1,2,3])
    b = dsp_signal.Signal([4,1,2])

    mult_signal = a * b
    assert(mult_signal.signal[0, 0] == 4)
    assert(mult_signal.signal[0, 1] == 2)
    assert(mult_signal.signal[0, 2] == 6)
