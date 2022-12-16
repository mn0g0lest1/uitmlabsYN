import numpy as np

tab_1 = [2**i for i in range(7, -1, -1)]
print(f"{tab_1}\n")
wagi = np.array(tab_1)
print(f"{wagi}\n")
liczba_bin = np.random.randint(low=0, high=2, size=8)
print(f"{liczba_bin}\n")
bin_dec = liczba_bin * wagi
print(f"{bin_dec}\n")
print(f"{bin_dec.sum()}")
