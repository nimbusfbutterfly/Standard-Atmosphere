import numpy as np
import matplotlib.pyplot as plt
from ambiance import Atmosphere

# Create an atmosphere object
heights = np.linspace(-5e3, 80e3, num=1000)
atmosphere = Atmosphere(heights)

# Make plot
plt.plot(atmosphere.pressure, heights/1000)
plt.ylabel('Height [km]')
plt.xlabel('pressure [pa]')
plt.grid()
plt.show()