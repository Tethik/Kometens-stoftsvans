from numpy import *
import matplotlib.pyplot as plt
from mathdefs import *

def plotElipse(start, end):
    positions = [position(angle) for angle in arange(start, end, 0.01)]
    x, y = [x for x,_ in positions], [y for _,y in positions]
    plt.plot(x,y) # elipse
    plt.axhline(0, color="grey")
    plt.axvline(0, color="grey")
    
    current = 2*pi/3
    
    x, y = position(current)
    plt.plot(x, y, 'rs') # kometen
    plt.plot(0, 0, 'yo') # solen    
    
    d = direction(current)
    dl = linalg.norm(d)
    d = (d[0] / dl, d[1] / dl)
    #~ length_of_line = 50
    #~ plt.plot([x + d[0] * l for l in xrange(length_of_line)],[y + d[1] * l for l in xrange(length_of_line)])
    
    
    plt.show()



def main():
    plotElipse(0,2*pi)

if __name__ == '__main__':
    main()
