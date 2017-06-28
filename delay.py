import numpy as np

def delay(a, dt=0):
    if dt==0:
        return a
    elif dt>0:
        rand = np.random.rand(dt)
        d = np.concatenate((rand, a[:-rand.shape[0]]), axis=0)
        return d
