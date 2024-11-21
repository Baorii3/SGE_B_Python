print("El bucle for")
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
par = []
impar = []
for x in num:
    if x%2 == 0:
        par.append(x)
    else:
        impar.append(x)
print(par)
print(impar)