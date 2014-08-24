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


def plot(z, stoftar):	
	x = [k for k,_,_,_ in z]
	y = [r for _,r,_,_ in z]
	
	fig, ax = plt.subplots()
	ax.plot(x, y)
	
	for stoft in stoftar:
		x = [k for k,_,_,_ in stoft]
		y = [r for _,r,_,_ in stoft]
		ax.plot(x, y, 'r')
	
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
		
	def _curveDistanceToPoint(point, curve):
		prevdiff = diff = _length((p0[0] - x, p0[1] - y))
		while diff <= prevdiff and i < len(g):
			prevdiff = diff			
			x, y, vx, vy = g[i]	
			i += 1	
			diff = _length((p0[0] - x, p0[1] - y))	
		i -= 1
		x, y, vx, vy = g[i]
		return _length((p0[0] - x, p0[1] - y))
		
	def _getZeroPoint(curve):
		x, y, _, _ = curve[0]
		prev = abs(y)
		i = 1
		while y >= 0 and i < len(curve):
			x, y, _, _ = curve[i]
			#~ print x,y
			i += 1
		i -= 1
		return curve[i]
		
	
	diff = 1
	delta = 0.1
	angle = 2*pi/3
	while diff > desired_accuracy:
		curve = generateData(C, angle, v, 3000) # -0.085			
		
		#~ _curveDistanceToPoint(p0, g)
		zero = _getZeroPoint(curve)
		print zero
		if zero[0] > p0[0]:
			v += delta
		elif zero[0] < p0[0]:
			v -= delta
				
		diff = _length((p0[0] - zero[0], p0[1] - zero[1]))
		delta /= 2
		print diff, v
		#~ break
		
	cvals = arange(-1, 1, 0.1)	
	stoftar = [generateData(c, angle, v, 3000) for c in cvals]
	plot(curve, stoftar)
	

if __name__ == '__main__':
	main()
