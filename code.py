import numpy as np
import matplotlib.pyplot as plt

# Set up the figure
plt.figure(figsize=(6,6))

# Define the theta values (angle)
theta = np.linspace(0, 2 * np.pi, 1000)

# Define the rose curve with the equation r = sin(n * theta)
n = 5  # Controls the number of petals
r = np.sin(n * theta)

# Create the polar plot
ax = plt.subplot(111, projection='polar')

# Plot the rose curve
ax.plot(theta, r, color='red', lw=2)

# Add gridlines for better visuals
ax.grid(True)

# Show the plot
plt.show()
