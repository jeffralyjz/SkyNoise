import numpy as np
import matplotlib.pyplot as plt

def delay(a, dt=0):
    if type(dt)==int:

        print 'Used concatenate'

        if dt==0:
            #With delay zero, the array should remain
            #unchanged.
            return a

        elif dt>0:
            rand = np.random.rand(dt)
            # d is the shifted original array
            # ex. if original = [A,B,C] i = 2
            # then d_original = [rand1, rand2, A]
            d = np.concatenate((rand, a[:-rand.shape[0]]), axis=0)
            return d

    elif type(dt)==float:

        print 'Used FFT'

        #Fourier transform f
        f_fft=np.fft.fft(a)

        #returns cycles per second if sample spacing of f is 
        #in seconds
        nu = np.fft.fftfreq(a.shape[0])

        #Phase shift(kronecker delta)
        phi = np.exp(-2*np.pi*1j*nu*dt)

        #Convolving f with phi
        fsh = np.fft.ifft(phi*f_fft)

        #Must take the real since original fct is real
        fshr = fsh.real

        return fshr

