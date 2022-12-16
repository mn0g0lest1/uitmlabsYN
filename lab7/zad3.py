import numpy as np
a = np.zeros((3,3))
b = np.zeros((3,3))
c = np.zeros((3,3))
d = np.zeros((3,3))
e = np.zeros((3,3))

a[1:, :2] = 1
b[:, 2:] = 1
c[:2, :] = 1
d[:2, 0] = 1
e[:2, [0, 2]] = 1

print(f"{a}\n")
print(f"{b}\n")
print(f"{c}\n")
print(f"{d}\n")
print(f"{e}")