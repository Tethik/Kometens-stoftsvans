import scipy.integrate as integrate
import matplotlib.pyplot as plt
from numpy import *
from mathdefs import *
from svans import *
import os

v = -0.0850769519806 
angle = 2*pi/3

def generateFrames(t):
	C = 1
	curve = generateData(C, angle, v, t)
	cvals = arange(-1, 0.99, 0.1)
	stoftar = [generateData(c, angle, v, t) for c in cvals]
	
	try:
		os.mkdir("frames")
	except:
		pass
	

	fig = plt.figure()
	ax = plt.axes(xlim=(-200,200), ylim=(-200,200))
	line, = ax.plot([], [])
	
	for stoft in stoftar: 
		for i in xrange(1,10):
			ax.plot(stoft[len(stoft)-i*100][0], stoft[len(stoft)-i*100][1], 'rx', alpha=1.0 - (0.1*i))	
	ax.plot(0, 0, 'yo') # solen 
	ax.set_aspect('equal')
	
	def animate(i):
		x = [k for k,_,_,_ in curve[:i*50]]
		y = [r for _,r,_,_ in curve[:i*50]]
		line.set_data(x,y)
		return line,
		
	from matplotlib import animation

	# call the animator.  blit=True means only re-draw the parts that have changed.
	anim = animation.FuncAnimation(fig, animate, frames=t / 50, interval=100, blit=True)	
	print "Now trying to save..."
	anim.save('basic_animation.mp4')
	
		
generateFrames(10000)
	
		
