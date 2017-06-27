import numpy as np

def delay(a, dt=0):
    rand = np.random.rand(dt)
    randsh = rand.shape
    d = np.concatenate((rand, a[randsh[0]:]), axis=0)
    return d
