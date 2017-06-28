import numpy as np

def delay(a, dt=0):
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
