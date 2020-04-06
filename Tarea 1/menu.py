
menu = '''
========= Menu ========
1. Admin
2. Dev
3. Gerente
4. Cliente
5. Salir
'''

print(menu)

message = '   Bienvenido '

while True:
    opcion = int(input('Ingrese su usuario: '))
    if opcion is 1:
        print(f'{message} Admin')
    elif opcion is 2:
        print(f'{message} Dev')
    elif opcion is 3:
        print(f'{message} Gerente')
    elif opcion is 4:
        print(f'{message} Cliente')
    elif opcion is 5:
        print(' *** Programa Finalizado ***')
        break
    else :
        print(f'Opción {opcion}  no disponible')

#fin
