import numpy as ny
import matplotlib.pyplot as plt
x=ny.arange(4,-4,0.01)
y1=x**2
y2=-x**2
y3=(x-1)**2
y4=x**2-1


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.show()

