print('  --- Porgrama Para invertir un numero ---')

numero = input('Ingrese un numero: ')
numero_invertido = ''

for indice in range(len(numero), 0, -1) :
    numero_invertido += numero[indice - 1]


print('  - El numero ingresado es: ', numero)
print('  - El numero invertido es: ', numero_invertido)