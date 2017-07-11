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
    assert (0 <= dt < a.size) #delay out of possible range
    if mode =='wcon':
        assert(type(dt) in (int, long))#To do float type delays use wfft
        d_a = np.concatenate((a[dt-a.size:],a[:dt]))
        return d_a
    elif mode=='ncon':
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
'''This function serves to create multiple arrays that are delayed by some random amount.
signals: Number of desired signal arrays
elem: number of elements in signal array
ld: lowest delay
hd: highest delay
'''
def mult(signals, elem, tau='n'):
    assert tau in ('n' , 'rand', 'choose')
    n = np.random.randn(signals, elem)
    if tau == 'n':
        return n
    if tau == 'rand':
        ld = input('Enter minimum delay: ')
        hd = input('Enter max delay: ')
        for i in range(signals):
            r = np.random.randint(ld, hd)
            n[i]= delay(n[i], r, 'wfft')
        return n
    if tau =='choose':
        for i in range(signals):
            print 'Delay array ' , i+1 , ' by: '
            r = input()
            n[i]= delay(n[i], r, 'wfft')
        return n
