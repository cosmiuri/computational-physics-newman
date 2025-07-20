import numpy as np

data = np.loadtxt('stm.txt')

print(data[:10])

import matplotlib.pyplot as plt

plt.imshow(data,origin = 'lower')
plt.show()