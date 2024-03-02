import numpy as np
import matplotlib.pyplot as plt
from ambiance import Atmosphere

# Create an atmosphere object
heights = np.linspace(-5e3, 80e3, num=1000)
atmosphere = Atmosphere(heights)

# Make plot
plt.plot(atmosphere.kinematic_viscosity, heights/1000)
plt.ylabel('Height [km]')
plt.xlabel('Kinematic Viscosity [m^2/s]')
plt.grid()
plt.show()