import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.random.randn(40)
y = np.random.randn(40)
z = np.random.randn(40)
colors = np.random.randn(40)
# use the scatter function
plt.scatter(x, y, s = z * 1000, c = colors)
plt.show()
