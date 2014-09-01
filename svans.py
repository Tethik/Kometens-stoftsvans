import scipy.integrate as integrate
import matplotlib.pyplot as plt
from numpy import *
from mathdefs import *

def generateData(C, angle, V0, tmax):
	k0 = direction(angle)
	v0 = inner(k0, V0)
	z0 = position(angle)
	
	def _z_bis(z, t):
		x,y,dx,dy = z				
		d = -C / (sqrt(x**2 + y**2)**3)
		return [dx, dy, x * d, y * d]
	
	t_output = arange(0, tmax, 1)
	
	z = integrate.odeint(_z_bis, [z0[0], z0[1], v0[0], v0[1]], t_output)
	return z


def plot(z, stoftar):	
	x = [k for k,_,_,_ in z]
	y = [r for _,r,_,_ in z]
	
	fig, ax = plt.subplots()
	ax.plot(x, y)
	
	for stoft in stoftar: 
		for i in xrange(1,10):
			ax.plot(stoft[len(stoft)-i*100][0], stoft[len(stoft)-i*100][1], 'rx', alpha=1.0 - (0.1*i))
	
	ax.plot(75, 0, 'x')
	ax.plot(0, 0, 'yo') # solen   
	ax.set_aspect('equal')
	plt.grid(True)
	plt.show()


def main():
	def _length(vec):
		return sqrt(vec[0] ** 2 + vec[1] ** 2)
		
	def _getZeroPoint(curve):
		x, y, _, _ = curve[0]
		prev = abs(y)
		i = 1
		while y >= 0 and i < len(curve):
			x, y, _, _ = curve[i]			
			i += 1
		i -= 1
		return (i,curve[i])
	
	C = 1		
	desired_accuracy = 0.0001
	v0 = -0.1
	p0 = (75, 0)	
	v = v0
	
	diff = 1
	delta = 0.1
	angle = 2*pi/3
	while diff > desired_accuracy and delta > 0:
		curve = generateData(C, angle, v, 300000) # -0.085			
		
		t, zero = _getZeroPoint(curve)
		print zero
		if zero[0] > p0[0]:
			v += delta
		elif zero[0] < p0[0]:
			v -= delta
				
		diff = abs(p0[0] - zero[0]) # _length((p0[0] - zero[0], p0[1] - zero[1]))
		delta /= 2
		print diff, v, delta
		
	cvals = arange(-1, 0.99, 0.1)	
	curve = generateData(C, angle, v, t) # -0.085
	print t
	stoftar = [generateData(c, angle, v, t) for c in cvals]
	plot(curve, stoftar)
	

if __name__ == '__main__':
	main()
