from numpy import *
import matplotlib.pyplot as plot

E = 0.4
R = 105


def plotElipse(start, end):
    positions = [elipsePosition(angle) for angle in arange(start, end, 0.01)]
    x, y = [x for x,_ in positions], [y for _,y in positions]
    plot.plot(x,y)
    plot.axhline(0, color="grey")
    plot.axvline(0, color="grey")
    plot.show()

def elipseRadius(angle):
    return R/(1+E*cos(angle))

def elipsePosition(angle):
    r = elipseRadius(angle)
    return (r*cos(angle),r*sin(angle))

def main():
    plotElipse(0,2*pi)

if __name__ == '__main__':
    main()