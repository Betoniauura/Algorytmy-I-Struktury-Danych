
#Zadanie 2

n = float(input("Długość ciągu"))
b = 0
while n > 0:
    n -= 1
    a = float(input("Podaj liczbę"))
    if a < 0:
        b += 1

print("Ilość liczb ujemnych:",b)
