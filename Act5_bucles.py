print("El bucle for")
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
sumapar = 0
sumaimpar = 0
for x in num:
    if x%2 == 0:
        sumapar+=x
    else:
        sumaimpar+=x
print(sumapar)
print(sumaimpar)