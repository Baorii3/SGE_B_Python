nota = float(input("Nota: "))

if 0 <= nota < 5:
    print("L'alumne ha suspès.")
elif 5 <= nota <= 6.5:
    print("L'alumne ha aprovat.")
elif 6.5 < nota <= 8:
    print("L'alumne té un notable.")
elif nota > 8:
    print("L'alumne té un excel·lent.")
else:
    print("Nota no vàlida.")
