import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np


pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin

# (u, k)
def deriv_z(z, t):
	print z, t
	k, r = z
	d = 0.01 * k * r
	return [2*k - d, -r + d]

z0 = [300, 150]
t = np.linspace(0, 9, 5000)
z = integrate.odeint(deriv_z, z0, t)
kaniner = [k for k,_ in z]
ravar = [r for _,r in z]
print z
fig, ax = plt.subplots()
ax.plot(t, kaniner)
ax.plot(t, ravar)
#~ ax.set_aspect('equal')
plt.grid(True)
plt.show()

if __name__ == "__main__":
	print "woot"
