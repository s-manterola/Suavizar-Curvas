# Math
from cProfile import label
import sys
sys.path.append('/home/seba/Documents/Python/Math')

from pycoingecko import CoinGeckoAPI
from datetime import datetime
import matplotlib.pyplot as plt
import Suavizar_curva as sc
import numpy as np

def getCurve(id, coin, days):
    cg = CoinGeckoAPI()
    
    fecha = []
    precio = []    

    for i in cg.get_coin_market_chart_by_id(id = id, vs_currency = coin, days = days)['prices']:
        fecha.append(i[0]/1000)
        precio.append(i[1])
        

    return fecha, precio

class Main():
    id = 'bitcoin'
    coin = 'usd'
    days = '190'

    x, Y = getCurve(id, coin, days)

    den = 1 + 1/(250*len(x))

    xfecha = []
    for i in x:
        xfecha.append(datetime.fromtimestamp(i))

    adp = sc.Fourier(x, Y, den)

    plt.plot(xfecha, Y, '-g', label = "Precio BitCoin")
    plt.plot(xfecha, adp, '-r', label = "Smoothen Curve")
    plt.legend()
    plt.grid()
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Price of BitCoin and a Smoothen Curve")
    plt.show()