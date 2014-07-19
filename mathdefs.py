from numpy import *

E = 0.4
R = 105


def direction(angle):
	rp = radiusDeriv(angle)
	r = radius(angle)
	c = cos(angle)
	s = sin(angle)
	return (rp * c - r * s, rp * s + r * c)

def radiusDeriv(angle):
	return R * (E * sin(angle)) / ((1 + E * cos(angle))**2)

def radius(angle):
    return R/(1+E*cos(angle))

def position(angle):
    r = radius(angle)
    return (r*cos(angle),r*sin(angle))
