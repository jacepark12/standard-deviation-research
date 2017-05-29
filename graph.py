import numpy as np
import matplotlib.pyplot as plt

v = []
for i in range(1, 11):
    v.append(i)

v.append(100)

print(v)
print(np.mean(v))
print(np.std(v))
plt.margins(y=.1, x=.1)

plt.plot(v, 'ro')
plt.show()

print(np.median(v))

print(np.average(v))
