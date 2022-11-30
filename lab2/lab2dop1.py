# Zadanie 1. Wyznaczanie wartości liczby zapisanej w systemie pozycyjnym o podstawie 𝑝 ∈ {2, … ,10}. Wartość
# liczby – liczba zapisana w systemie dziesiętnym. Na wejściu podajemy liczbę jako string, na wyjściu – liczbę
# dziesiętną typu int.

p = input("Enter number 2-10: ")
s = int(p)
if s >= 2 and s <= 10:
    print(s)
else:
    print("Error rerun and enter number 2-10")



# print(type(s))
