# 2D Line Plot Basics

import matplotlib.pyplot as plt

hours = [0, 1, 2, 3, 4, 5]
temperature = [30, 32, 34, 33, 31, 29]

plt.plot(hours, temperature)
plt.xlabel('Hours')
plt.ylabel('Temperature')
plt.title('Temperature vs. Hours')
plt.show()

# Customize the plot
plt.grid(True)
plt.tight_layout()

# plotting multiple lines
humidity = [70, 65, 60, 62, 68, 72]
plt.plot(hours, temperature, label='Temperature', color='blue', marker='o')
plt.plot(hours, humidity, label='Humidity', color='green', marker='x')
plt.xlabel('Hours')
plt.ylabel('Values')
plt.title('Temperature and Humidity vs. Hours')
plt.legend()
