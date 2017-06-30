import numpy as np


#This function delays the f array by a decimal amount
def tau(f, tau, graph = 'n')
    #Fourier transform f
    f_fft=np.fft.fft(f)
    
    #returns cycles per second if sample spacing of f is 
    #in seconds
    nu = np.fft.fftfreq(f.shape[0})
    
    #Phase shift(kronecker delta)
    phi = np.exp(-2*np.pi*1j*nu*tau)

    #Convolving f with phi
    fsh = np.fft.ifft(phi*f_fft)

    if graph =='n':
        return fsh
    elif graph =='y':
        return plt.plot(fsh, c='r'), plt.plot(f, c='g')

