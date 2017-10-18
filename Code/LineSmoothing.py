# LineSmoothing.py
#
# Smooths a 1D line using a convolution of the initial line
# 
# See numpy documentation for complete documentation on methods used

import numpy as np

def smooth(x, window_len=11, window='hanning'):
    """Smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    Args
    ----
    x : iter
        Some 1D signal (list, np.ndarray, etc.)

    Keyword Args
    ------------
    window_len : int
        the dimension of the smoothing window; should be an odd integer
    window : str
        type of window from 'flat', 'hanning', 'hamming', 'bartlett',
        'blackman'; flat window will produce a moving average

    Returns
    -------
    numpy.ndarray
        Smoothed array of same length as `x` input
        
    Example
    -------
    t = linspace(-2, 2, 0.1)
    x = sin(t) + randn(len(t)) * 0.1
    y = smooth(x)
    
    See also
    --------
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
    """
    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")
    if window_len < 3:  # Cannot solve under 3
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[x[window_len-1:0:-1], x, x[-2:-window_len-1:-1]]
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.' + window + '(window_len)')
    y = np.convolve(w / w.sum(), s, mode='valid')
    # Odd window lengths require shift to ensure size remains the same as x
    odd_shift = window_len % 2
    # Slice of ends of convolution
    return y[(window_len // 2):(len(y) - window_len // 2 + 1 - odd_shift)]


from numpy import *
from pylab import *

def smooth_demo():
    """pylab-based graphing demo for each smoothing window"""
    t = linspace(-4, 4, 100)
    x = sin(t)
    xn = x + randn(len(t)) * 0.1
    y = smooth(x)

    ws = 31

    subplot(211)
    plot(ones(ws))

    windows=['flat', 'hanning', 'hamming', 'bartlett', 'blackman']

    for w in windows[1:]:
        eval('plot(' + w + '(ws) )')

    axis([0, 30, 0, 1.1])

    legend(windows)
    title("The smoothing windows")
    subplot(212)
    plot(x)
    plot(xn)
    for w in windows:
        plot(smooth(xn, 10, w))
    l = ['original signal', 'signal with noise']
    l.extend(windows)

    legend(l)
    title("Smoothing a noisy signal")
    show()


if __name__=='__main__':
    smooth_demo()