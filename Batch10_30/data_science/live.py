import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation
#%matplotlib notebook 
x = list(np.arange(1,11))
y = list(np.random.randint(10,25,10))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x,y,'r^:')

import time
def change(interval):
    global x,y
    y.pop(0)
    y.append(np.random.randint(10,25))
    time.sleep(interval)
    ax.clear()
    ax.plot(x,y,'r^:')
    
ani = FuncAnimation(fig,change,1)
plt.show()

