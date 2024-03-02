from ambiance import Atmosphere

print("{:^10} | {:^15} | {:^15} | {:^20} | {:^25} | {:^25}".format(
    "Altitude", "Temperature", "Pressure", "Density", "Atmospheric Kinetic Viscosity", "Speed of Sound"))
print("-" * 135)

altitudes = list(range(0, 30480, 100))  # in meters
atm = Atmosphere(altitudes)

for i in range(len(altitudes)):
    print("{:>10,.0f} | {:>15.8f} | {:>15.8f} | {:>20.8f} | {:>29.8f} | {:>25.8f}".format(
        altitudes[i], atm.temperature[i], atm.pressure[i], atm.density[i], atm.kinematic_viscosity[i], atm.speed_of_sound[i]))


