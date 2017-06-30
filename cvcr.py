import numpy as np

def cvcr(f,g, cvcr = 'conv'):
    #fourier transform functions
    f_fft = np.fft.fft(f)
    g_fft = np.fft.fft(g)

    if cvcr == 'conv':
        return np.fft.ifft(f_fft*g_fft)
    elif cvcr == 'corr':
        return np.fft.ifft(f_fft*g_fft.conj())
