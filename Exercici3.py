"""Programa que introdueixes 2 numeros i et diu quin numero es major"""
NUMERO1 = int(input("Escriu el primer numero"))
NUMERO2 = int(input("Escriu el segon numero"))
if NUMERO1 > NUMERO2:
    print("El primer numero es major que el segon numero")
else:
    if NUMERO1 < NUMERO2:
        print("El segon numero es major que el primer numero")
