import sys
sys.path.append('/home/seba/Documents/Python/Math')

from pycoingecko import CoinGeckoAPI
from datetime import datetime
import matplotlib.pyplot as plt
import Transformadas as sf
import numpy as np




def Densidad(x, y):
    ret = 0
    for i in range(len(x)-1):
        ret += np.sqrt((y[i+1]-y[i])**2 + (x[i+1] - x[i])**2)
            
    return ret/np.sqrt((y[-1]-y[0])**2 + (x[-1] - x[0])**2)


def Fourier(x, Y, denmax):
    ret = 0

    m = (Y[-1]-Y[0])/(x[-1]-x[0])
    Y0 = Y[0]
    C = []
    y=[]
    
    for i in range(len(x)):
        C.append(m*(x[i]-x[0]) + Y0)
        y.append(Y[i] - C[i])

    den = Densidad(x, y)
    if den < denmax:
        ret = y
    else:
        men = 1
        ymen = sf.Fourier(x, y, men)
        dmen = Densidad(x, ymen)
        
        sup = 100
        ysup = sf.Fourier(x, y, sup)
        dsup = Densidad(x, ysup)
        
        while(True):
            m = int((men+sup)/2)
            ym = sf.Fourier(x, y, m)
            dm = Densidad(x, ym)
            
            if (dm == denmax):
                ret = ym
                break
            
            elif((men - sup)**2 == 1):
                if (denmax - dmen)**2 < (denmax - dsup)**2:
                    ret = ymen
                    break
                else:
                    ret = ysup
                    break
            
            elif dm < denmax:
                men = m
                ymen = ym
                dmen = dm
            
            elif dm > denmax:
                sup = m
                ysup = ym
                dsup = dm
    
    r = []
    for i in range(len(x)):
        r.append(ret[i] + C[i])
    
    return r