import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)

a = 1
b = -2
c = 0
temperature = a * months**2 + b * months + c

max_temp = max(temperature)
min_temp = min(temperature)
temperature = 1 + (temperature - min_temp) * (49) / (max_temp - min_temp)

plt.figure(figsize=(10, 5))
plt.plot(months, temperature, label='Temperature (°C)', marker='o')
plt.xlabel('Time (Months)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over 12 Months')
plt.ylim(1, 50)
plt.legend()
plt.grid(True)
plt.show()