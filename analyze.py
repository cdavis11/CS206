import numpy as np
import matplotlib.pyplot

# Load and print back and fron leg sensor value data
backLegSensorValues = np.load('data/backLegSensorValues.npy')
print(backLegSensorValues)
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
print(frontLegSensorValues)

# Plot data
matplotlib.pyplot.plot(backLegSensorValues, linewidth=3, label="back leg sensor")
matplotlib.pyplot.plot(frontLegSensorValues, label= "front leg sensor")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
