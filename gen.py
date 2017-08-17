import numpy as np
import scipy
import aipy
import linsolve as ls
import collections
import Combinatorics

def gen(antcount, sigcount, datasize, bins, samples, clk_pr=5, dim = 1):
    """
    This function serves to generate multiple sources being measured by an antenna array.
    The minbase 
    """
    signals = np.random.randn(sigcount, datasize) # true signals
    minbase = np.array([np.random.rand() * 1e4, 0, 0]) # minimum baseline in one dim (cm)
    siglocs = np.random.rand(sigcount, 3) # unit vector pointing at source location
    Siglocs = []
    for i in range(sigcount):
        sign1 = (-1) ** np.random.randint(-1,1)
        if dim ==1: # all sources are restricted to the  xz plane
            sign2 = 0
        elif dim ==2: # sources are arbitrarily placed above the xy plane
            sign2 = (-1) ** np.random.randint(-1,1)
        Siglocs.append(siglocs[i] * np.array([sign1, sign2, 1])) # last sign is pos (above the horizon)
    siglocs = np.array(Siglocs) # TODO this was a quick fix
    delist = [] # delays of each signal based on siglocs
    gains = [] # gain of each antenna
    for i in range(sigcount): # delay of each source
        delist.append(np.dot(minbase, siglocs[i]) / aipy.const.len_ns / clk_pr) 
    for i in range(antcount): # gains of each antenna
        gains.append(np.random.uniform(.5,1.5))
    f_fft=np.fft.fft(signals) # fourier transform of signals
    nu = np.fft.fftfreq(datasize) # cycles per second
    delsig = [] # signals with delay corresponding to antenna position
    for i in range(sigcount):
        dt = delist[i] # extracting dt for each signal
        for k in range(antcount):
            phi = np.exp(-2j * np.pi * nu * dt * k) # as desired, ant 1 has no delay (when k = 0)
            fcvp = np.fft.ifft(phi * f_fft)
            delsig.append(fcvp.real[i])
    delarr= np.array(delsig) # delayed signals array
    measig = [] # antennas' measured data 
    for i in range(antcount):
        measig.append(gains[i] * np.sum(delsig[i::antcount], axis = 0)) # sum of signals multd by gains to simulate measurement of each antenna
    msig = np.array(measig) # easier (for me) to reshape a np array
    new = [] # new list of reshaped msig
    for i in range(antcount):
        new.append(np.reshape(msig[i], (bins, samples)))
    fftmeasig = np.fft.rfft(new) # fourier transform of all the measured signal arrays
    mvis=[] # measured visbilities 
    for i in range(antcount):
        for k in range(antcount):
            if i<k: # ensures unique pairs 
                mvis.append(fftmeasig[i] * fftmeasig[k].conj())
    finvis = [] # final visibilities
    for i in range(antcount * (antcount - 1) / 2):
        finvis.append(np.average(mvis[i], axis=0))
    return np.array(finvis)
