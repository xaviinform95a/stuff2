"""Programa on introdueixes 2 numeros i et diu si el primer numero es igual o no"""
NUMERO1 = int(input("Escriu el primer numero"))
NUMERO2 = int(input("Escriu el segon numero"))
if NUMERO1 == NUMERO2:
    print("El numero", NUMERO1, "es igual que el numero", NUMERO2)
else:
    if NUMERO1 != NUMERO2:
        print("El numero", NUMERO1, " no es igual que el numero", NUMERO2)
