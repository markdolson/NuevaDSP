import dsp_signal

def test_addition():
    a = dsp_signal.Signal([1,2,3])
    b = dsp_signal.Signal([4,1,2])

    sum_signal = a + b
    assert(sum_signal.signal[0, 0] == 5)
    assert(sum_signal.signal[0, 1] == 3)
    assert(sum_signal.signal[0, 2] == 5)

def test_scalar_addition():
    a = dsp_signal.Signal([1,2,3]) + 6
    assert(a.signal[0, 0] == 7)
    assert(a.signal[0, 1] == 8)
    assert(a.signal[0, 2] == 9)

def test_mult():
    a = dsp_signal.Signal([1,2,3])
    b = dsp_signal.Signal([4,1,2])

    mult_signal = a * b
    assert(mult_signal.signal[0, 0] == 4)
    assert(mult_signal.signal[0, 1] == 2)
    assert(mult_signal.signal[0, 2] == 6)

def test_scalar_mult():
    a = dsp_signal.Signal([1,2,3]) * 2
    assert(a.signal[0, 0] == 2)
    assert(a.signal[0, 1] == 4)
    assert(a.signal[0, 2] == 6)

def test_shift():
    a = dsp_signal.Signal([1,2,3])
    a = a.shift(1)

    assert(a.signal[0, 0] == 0)
    assert(a.signal[0, 1] == 1)
    assert(a.signal[0, 2] == 2)

    a = a.shift(-2)

    assert(a.signal[0, 0] == 2)
    assert(a.signal[0, 1] == 0)
    assert(a.signal[0, 2] == 0)

def test_clip():
    a = dsp_signal.Signal([1,2,3])
    a = a.clip(1,2)
    assert(a.signal[0,0] == 2)

def test_concatenate():
    a = dsp_signal.Signal([1,2,3])
    a = a.concatenate(a)

    assert(a.signal[0, 0] == 1)
    assert(a.signal[0, 1] == 2)
    assert(a.signal[0, 2] == 3)
    assert(a.signal[0, 3] == 1)
    assert(a.signal[0, 4] == 2)
    assert(a.signal[0, 5] == 3)

