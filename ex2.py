dia_setmana = input("Dia setmana: ")
dias_setmana = ["dilluns","dimarts","dimecres","dijous","divendres","dissabte","diumenge"]
if dia_setmana in dias_setmana:
    print(f"Avui es {dia_setmana}")
else:
    print("Dia no valid")