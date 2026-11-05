# 2d line from pandas dataframe
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Hours': [0, 1, 2, 3, 4, 5],
    'Temperature': [30, 32, 34, 33, 31, 29],
    'Humidity': [70, 65, 60, 62, 68, 72]
}

df = pd.DataFrame(data)

# Plotting Temperature vs Hours
plt.plot(df['Hours'], df['Temperature'], label='Temperature', color='blue', marker='o')
plt.xlabel('Hours')
plt.ylabel('Temperature')
plt.title('Temperature vs. Hours')
plt.show()

# Plotting Humidity vs Hours
plt.plot(df['Hours'], df['Humidity'], label='Humidity', color='green', marker='x')
plt.xlabel('Hours')
plt.ylabel('Humidity')
plt.title('Humidity vs. Hours')
plt.legend(loc='upper right')
plt.show()
