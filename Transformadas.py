import numpy as np
import matplotlib.pyplot as plt
from Integral1D import *

def Fourier(x, y, n):
    T = x[-1]-x[0]
    a0 = (2/T) * Simpson(x, y)
    
    a = [0]
    b = [0]
    for i in range(1,n):
        fa = []
        fb = []
        for j in range(len(x)):
            fa.append(y[j]*np.cos(2*np.pi*i*x[j]/T))
            fb.append(y[j]*np.sin(2*np.pi*i*x[j]/T))
        a.append((2/T)*Simpson(x, fa))
        b.append((2/T)*Simpson(x, fb))
        
    ret = []
    for j in range(len(x)):
        aux = a0/2
        for i in range(1,n):        
            aux += a[i]*np.cos(2*np.pi*i*x[j]/T) + b[i]*np.sin(2*np.pi*i*x[j]/T)
        ret.append(aux)

    return ret


