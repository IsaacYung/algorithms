from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)

plt.figure(figsize=(10,8))
plt.ylim(0, 100)
plt.plot(n, np.ones(n.shape))
plt.show()
