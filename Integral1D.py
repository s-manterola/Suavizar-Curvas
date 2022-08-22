

def Simpson(x,y):
    ret = 0
    for i in range(len(x)-1):
        h = (x[i+1] - x[i])/6

        fab = (y[i] + y[i+1])/2
        ret += h*(y[i] + 4*fab + y[i+1])

    return ret