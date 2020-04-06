print('  --- Porgrama para generar los N numero primos ---')

cantidad = int(input('Ingrese un numero: '))

numeros_primos = ''
contador_primos = 1
numero = 2

while contador_primos <= cantidad :
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0 :
            es_primo = False
            break

    if es_primo :
        numeros_primos += ',' + str(numero)
        contador_primos += 1        
    
    numero += 1

print (f'> Los {cantidad} números primos son: ' ,numeros_primos[1 : len(numeros_primos)])