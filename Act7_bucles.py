while True:
    nombre = int(input("Nombre: "))
    if 100<=nombre<=400:
        print(f"El número {nombre} està dins del rang 100-400")
        break
    else:
        print("Torna a intentar")
