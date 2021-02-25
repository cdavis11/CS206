import numpy as np
import matplotlib.pyplot

# Load and print back and front leg sensor value data, target angles
backLegSensorValues = np.load('data/backLegSensorValues.npy')
print(backLegSensorValues)
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
print(frontLegSensorValues)
targetAnglesBackLeg = np.load('data/targetAngleValuesBackLeg.npy')
targetAnglesFrontLeg = np.load('data/targetAngleValuesFrontLeg.npy')

# Plot data
matplotlib.pyplot.plot(backLegSensorValues, linewidth=3, label="back leg sensor")
matplotlib.pyplot.plot(frontLegSensorValues, label= "front leg sensor")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

matplotlib.pyplot.plot(targetAnglesBackLeg, label="Back Leg Motor values")
matplotlib.pyplot.plot(targetAnglesFrontLeg, label="Front Leg Motor values")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
