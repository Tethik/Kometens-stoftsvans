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

	fig = plt.figure()
	ax = plt.axes(xlim=(-200,200), ylim=(-200,200))
	line, = ax.plot([], [])
	stoftlines = list()
	for _ in range( len(stoftar)):
		l, = ax.plot([], [])
		stoftlines.append(l)
	#~ print stoftlines
	
	ax.plot(0, 0, 'yo') # solen 
	ax.set_aspect('equal')
	
	def animate(i):
		x = [k for k,_,_,_ in curve[:i*50]]
		y = [r for _,r,_,_ in curve[:i*50]]
		line.set_data(x,y)
		
		
		for j in xrange(0,len(stoftlines)):
			stoftline = stoftlines[j]
			x = [k for k,_,_,_ in stoftar[j][:i*50]]
			y = [r for _,r,_,_ in stoftar[j][:i*50]]
			stoftline.set_data(x,y)
		
		return line,
		
	from matplotlib import animation

	# call the animator.  blit=True means only re-draw the parts that have changed.
	anim = animation.FuncAnimation(fig, animate, frames=t / 50, interval=100, blit=True)	
	print "Now trying to save..."
	anim.save('basic_animation.mp4')
	
		
generateFrames(10000)
	
		
