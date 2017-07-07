import numpy as np

'''Returns a shifted or wrapped array based on mode 
Example:

Shifts and wraps (Shifts only integer type delays)
>>>delay([1,2,3,4,5], 3)
array([3,4,5,1,2])

Shifts and adds guassian noise 
>>>delay([1,2,3,4,5], 3, 'ncon')
array([randint, randint, randint, 1, 2])

'wfft' mode will shift and wrap an array via convolution theorem
This mode can handle float type delays 
'''
def delay(a, dt, mode='wcon'):
    assert (mode in ('wcon' , 'ncon', 'wfft')) #select mode from list
    assert (0 < dt < a.size) #delay out of possible range
    if mode =='wcon':
        assert(type(dt) in (int, long))#To do float type delays use wfft
        d_a = np.concatenate((a[dt-a.size:],a[:dt]))
        return d_a
    elif mode=='nconc':
        assert(type(dt) in (int, long))#To do float type delays use wfft
        rand = np.random.rand(dt)
        d_a = np.concatenate((rand, a[:-rand.size]), axis=0)
        return d_a
    elif mode=='wfft': # TODO Improve Tolerance
        f_fft=np.fft.fft(a)
        #returns cycles per second if sample spacing of f is in seconds
        nu = np.fft.fftfreq(a.size)
        #Phase shift(kronecker delta)
        phi = np.exp(-2j*np.pi*nu*dt)
        fcvp = np.fft.ifft(phi*f_fft)
        d_a = fcvp.astype(a.dtype)
        return d_a
