import numpy as np

"""Convolves or correlates to arrays.
op is operation type.
scv = Return array in original array units(convolution thm)
scr = return correlation between the two arrays by conjugating the second
hcv = similiar to scv but ignores inverse fourier transform and returns array in 'Hz'
hcr = similiar to scr but ignores the inverse fourier transform"""

def cvcr(f,g, op='scv'):
    assert (op in ('scv','scr','hcv','hcr'))
    #fourier transform functions
    f_fft = np.fft.fft(f)
    g_fft = np.fft.fft(g)
    fg = f_fft*g_fft
    fgc = f_fft*g_fft.conj()
    if op=='scv':
        fcvg = np.fft.ifft(fg)
        return fcvg
    elif op=='scr':
        fcrg = np.fft.ifft(fgc)
        return fcrg
    elif op=='hcv':
        return fg
    elif op=='hcr':
        return fgc

