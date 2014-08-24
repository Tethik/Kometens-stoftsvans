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
	
	def z_bis(z, t):
		x,y,dx,dy = z				
		d = -C / (sqrt(x**2 + y**2)**3)
		return [dx, dy, x * d, y * d]
	
	t_output = np.arange(0, tmax, 0.01)
	
	z = integrate.odeint(z_bis, [z0[0], z0[1], v0[0], v0[1]], t_output)		
		
	x = [k for k,_,_,_ in z]
	y = [r for _,r,_,_ in z]
	
	fig, ax = plt.subplots()
	ax.plot(x, y)
	
	ax.plot(75, 0, 'x')
	ax.plot(0, 0, 'yo') # solen   
	ax.set_aspect('equal')
	plt.grid(True)
	plt.show()


def main():
	C = 1
	
	plot(C, 2*pi/3, -0.085, 8700)
	

if __name__ == '__main__':
	main()
