#Zadanie 5


x = [[10,3,19,20],[20,14,2,4,80]]
for i in x:
    x.sort()
    for a in i:
        i.sort()
print("Minimalna wartość w pierwszym wierszu", x[0][0])
print("Minimalna wartość w drugim wierszu", x[1][0])

print(x) ''' #drugie zdanie zadania piątego,
             sort automatycznie przeniósł najmniejsze
             liczby na przód'''
