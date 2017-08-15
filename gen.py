import numpy as np
import scipy
import aipy
import linsolve as ls
import collections
import Combinatorics

def gen(antcount, sigcount, datasize, bins, samples, clk_pr=5, dim = 3):
    """ant = number of antennas
    src = number of sources
    """
    signals = np.random.randn(sigcount, datasize) # true signals
    minbase = np.array([np.random.rand(), 0, 0]) # minimum baseline in one dim
    siglocs = np.random.rand(sigcount, dim) # signal locations
    delist = [] # delays of each signal based on siglocs
    gains = [] # gain of each antenna
    for i in range(sigcount):
        delist.append(np.dot(minbase, siglocs[i]) / aipy.const.len_ns / clk_pr) 
    for i in range(antcount):
        gains.append(np.random.uniform(.5,1.5))
    f_fft=np.fft.fft(signals) # fourier transform of signals
    nu = np.fft.fftfreq(datasize) # cycles per second
    delsig = [] # signals with delay corresponding to antenna position
    for i in range(sigcount):
        dt = delist[i] # extracting dt for each signal
        for k in range(antcount):
            phi = np.exp(-2j * np.pi * nu * dt * k)
            fcvp = np.fft.ifft(phi * f_fft)
            delsig.append(fcvp.real[i])
    delarr= np.array(delsig)
    measig = [] # antennas' measured data 
    avg = []
    for i in range(antcount):
        measig.append(gains[i] * np.sum(delsig[i::antcount], axis = 0))
    msig = np.array(measig)
    new = []
    for i in range(antcount):
        new.append(np.reshape(msig[i], (bins, samples)))
    fftmeasig = np.fft.rfft(new) # fourier transform of all the measured signal arrays
    mvis=[]
    #for i in range(antcount):
    #   for k in range(antcount):
    #       if i!=k:
    #           print i,k
    #           mvis.append(fftmeasig[i] * fftmeasig[k].conj())
    comb = list(m_way_unordered_combinations(antcount, [2])) # produces the possible pairs of numbers
    pairs = []
    mvis = [] # measured visibilities 
    for i in range(len(comb)):
        pairs.append(comb[i][0][0])
        pairs.append(comb[i][0][1])
    for i in range(len(pairs) / 2):
        mvis.append(fftmeasig[pairs[2 * i]] * fftmeasig.conj()[pairs[2 * i + 1]])
    Mvis = np.array(mvis)
    finvis = []
    print Mvis[0].shape
    for i in range(Mvis.shape[0]):
        finvis.append(np.average(Mvis[i], axis=0))
    return np.array(finvis)
