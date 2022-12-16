import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
print(x)
plt.plot(x)
plt.plot(2 * np.sin(x))
plt.plot(2 + np.sin(x))
plt.plot(np.sin(2 * x))
plt.show()
