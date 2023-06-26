a = int(input("Podaj wartość do znalezienia: "))
tablica = [1, 2, 3, 4, 5]
x = 0
while x < len(tablica):
    if tablica[x] == a:
        print("Znaleziono wartość")
        break
    x += 1
else:
    print("Nie znaleziono wartości")