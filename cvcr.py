import numpy as np

def cvcr(f,g, cvcr = 'conv'):
    #fourier transform functions
    f_fft = np.fft.fft(f)
    g_fft = np.fft.fft(g)

    if cvcr == 'conv':
        fcvg = np.fft.ifft(f_fft*g_fft)
        fcvgr = fcvg.real
        return fcvgr
    elif cvcr == 'corr':
        fcrg = np.fft.ifft(f_fft*g_fft.conj())
        fcrgr = fcrg.real
        return fcrgr

