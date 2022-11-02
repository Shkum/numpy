import numpy as np

m = [i for i in range (12)]
print(m)

m = np.array(m)

m.shape = 3, 2, 2
print(m)
m.shape = (12,)
# m = m.tolist()
print(m)
