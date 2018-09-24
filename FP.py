import numpy as np
import matplotlib.pyplot as plt
#  form mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')


# make data
seg=24
u=np.linspace(0,2*np.pi,seg)
v=np.linspace(0,np.pi,seg)
x=10*np.outer(np.cos(u),np.sin(v))
y=10*np.outer(np.sin(u),np.sin(v))
z=10*np.outer(np.ones(seg),np.cos(v))

# Plot the surface
ax.plot_surface(x,y,z,color='red')

plt.show()
