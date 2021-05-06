#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    valores = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    suma = 0
    valor = 0
    for z in roman_string:
        if valores[z] > valor:
            suma = suma + valores[z] - valor * 2
        else:
            suma = suma + valores[z]
        valor = valores[z]
    return suma
