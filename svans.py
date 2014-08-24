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
	
	t_output = arange(0, tmax, 0.01)
	
	z = integrate.odeint(_z_bis, [z0[0], z0[1], v0[0], v0[1]], t_output)
	return z


def plot(z):	
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
	# Hitta (75,0) punkt. Ish. Newton Raphson.
	desired_accuracy = 0.001
	v0 = -0.1
	p0 = (75, 0)	
	v = v0
	
	def _length(vec):
		return sqrt(vec[0] ** 2 + vec[1] ** 2)
	
	diff = 1
	while diff > desired_accuracy:
		g = generateData(C, 2*pi/3, v, 8700) # -0.085			
		x, y, vx, vy = g[0]
		i = 1
		
		#~ prevdiff = diff = _length((p0[0] - x, p0[1] - y))
		prevdiff = diff = abs(75 - x)
		while diff <= prevdiff and i < len(g):
			prevdiff = diff			
			x, y, vx, vy = g[i]	
			i += 1	
			diff = abs(75 - x)
			#~ diff = _length((p0[0] - x, p0[1] - y))				
		
		i -= 1
		print g[i]			
		print p0
		x, y, vx, vy = g[i]
		diff = _length((p0[0] - x, p0[1] - y))
		print diff	
		v = v - ((y) / (vy))
		print v
		break
		
	plot(g)
	

if __name__ == '__main__':
	main()
