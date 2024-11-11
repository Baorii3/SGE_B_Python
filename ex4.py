salari = float(input("Salari: "))
iva = 0
if salari < 15000:
    iva = 0
    print(f"IVA 0%")
elif salari < 30000:
    iva = 10
    print(f"IVA 10%")
elif salari < 60000:
    iva = 21
    print(f"IVA 21%")

iva_dinero = salari*iva/100

print(f"Iva dinero {iva_dinero}")
print(f"Salari sense iva {salari-iva_dinero}")