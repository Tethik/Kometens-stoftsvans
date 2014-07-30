import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np
from mathdefs import *


pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin
inner = np.inner


def plot(C, angle, V0, tmax):	
	k0 = direction(angle)
	v0 = inner(k0, V0)
	z0 = position(angle)
	
	print k0
	print v0
	print z0
	
	b = True
	# (u, k)
	def z_bis(z, t):
		#~ print z
	
		x,y,dx,dy = z				
		d = -C / (sqrt(x**2 + y**2)**3)
		return [dx, dy, x * d, y * d]
	
	t_output = np.arange(0, tmax, 0.01)
	#~ h = 0.2
	#~ v, z = v0, z0
	#~ for i in xrange(0, tmax):
		#~ zbis = z_bis(z) # acceleration right now.
		#~ v = v + h / 6
		#~ z += inner(v, h)
	
	z = integrate.odeint(z_bis, [z0[0],z0[1],v0[0],v0[1]], t_output)		
	#~ print z
		
	x = [k for k,_,_,_ in z]
	y = [r for _,r,_,_ in z]
	#~ print z
	fig, ax = plt.subplots()
	ax.plot(x, y)
	
	#~ positions = [position(angle) for angle in np.arange(0,2*pi, 0.01)]
	#~ x, y = [x for x,_ in positions], [y for _,y in positions]
	#~ ax.plot(0,2*pi) # elipse
	
	ax.plot(75, 0, 'x')
	ax.plot(0, 0, 'yo') # solen   
	ax.set_aspect('equal')
	plt.grid(True)
	plt.show()


def plotSvans(start, end):
	positions = [position(angle) for angle in np.arange(start, end, 0.01)]
	x, y = [x for x,_ in positions], [y for _,y in positions]
	plt.plot(x,y) # elipse
	plt.axhline(0, color="grey")
	plt.axvline(0, color="grey")
	
	current = 2*pi/3
	
	x, y = position(current)
	
	
	plt.plot(x, y, 'rs') # kometen   
	plt.plot(0, 0, 'yo') # solen    
		
	plt.show()
	

def generate_Positions():
	t = 0
	dt = 1.0/40
	x, y = position(current)
	state = numpy.array([x,y])


def main():
	#~ plotSvans(0,2*pi)
	C = 1
	
	plot(C, 2*pi/3, -0.085, 8700)
	

if __name__ == '__main__':
	main()
