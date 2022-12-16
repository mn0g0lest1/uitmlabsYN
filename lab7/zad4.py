import numpy as np

a = np.zeros((5,5))

# def svitch_number(n):
#     a[:1, :] = n
#     a[:, :1] = n
#     a[4:, :] = n
#     a[:, 4:] = n
#     return a

# print(svitch_number(1))
# print(svitch_number(0))

a[:1, :] = 1
a[:, :1] = 1
a[4:, :] = 1
a[:, 4:] = 1

def svitch_number(n):
    # a[1:4, [1, 2, 3]] = n
    a[1:4, 1:4] = n
    return a

print(f"{a}\n")
print(f"{svitch_number(1)}\n")
print(svitch_number(0))




