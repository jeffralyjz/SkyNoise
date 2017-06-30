import numpy as np 

#Builds a tophat function
#t_coords must be an array
def tophat(t_coords, width, phi)
    out = t_coords.copy()
    for i, elem in enumerate(t_coords - phi):
        if abs(elem) > width:
            out[i]=0
        else:
            out[i]=1
    return out
