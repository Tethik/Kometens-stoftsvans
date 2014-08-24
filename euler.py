import matplotlib.pyplot as plt
import numpy as np


pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin


def f_biss(v, C):
    x, y = v
    return [(-C*x)/(s**3), (-C*y)/(s**3)]


def euler():    
    v0 = [0.0,0.0,  #x_0,y_0
          0.0,0.0]  #x'_0, y'_0

    #start values 
    v = [(v0[0], v0[1]),
         (v0[2], v0[3])]


    positions = []

    start = 0.0
    stop = 5.0
    steplength = 0.01
    stepnr = (stop-start)/steplength
    
    steps = np.linspace(start, stop, num=stepnr)

    for step in steps:
        v[1] = v[1] + np.dot(steplength,(2.0,2.0))
        v[0] = v[0] + np.dot(steplength,v[1])

        positions.append(v[0])

    x, y = [x for x,_ in positions], [y for _,y in positions]
    plt.plot(x,y) # elipse
    plt.axhline(0, color="grey")
    plt.axvline(0, color="grey")
    plt.show()

if __name__ == "__main__":
    euler()