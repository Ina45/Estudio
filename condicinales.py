"""
Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
hasta que se ingrese -1.
"""

numero_ingresado = 0
contador = 0

print('Ingrese un numero: ')
numero_ingresado = int(input())

while numero_ingresado != -1:
    contador = contador + numero_ingresado
    print('Ingrese un numero: ')
    numero_ingresado = int(input())

print("La suma es " + str(contador))


"""
2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que
0, menores que 0 e iguales a 0.
"""
numero_ingresado = 0
menores_cero = 0
cero = 0
mayores_cero = 0

print('Ingrese la cantidad de numeros a ingresar: ')
cantidad_numeros = int(input())
veces = 0

while veces < cantidad_numeros:
    veces +=1
    print('Ingrese un numero: ')
    numero_ingresado = int(input())
    if numero_ingresado == 0:
        cero += 1
    elif numero_ingresado > 0:
        mayores_cero += 1
    else:
        menores_cero +=1

print("Tengo "+ str(cero)+ " numeros iguales a 0")
print("Tengo "+ str(menores_cero)+ " numeros menores a 0")
print("Tengo "+ str(mayores_cero)+ " numeros mayores a 0")

"""
3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
contrario, el programa termina cuando se introduce un cero.
"""
vocales = ('a','e','i','o','u')

letra = input("Ingrese caracter: ")

while letra != '0':
    if letra in vocales:
        print('VOCAL')
    else:
        print('NO VOCAL')

    letra = input("Ingrese caracter ")


"""
4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos.
"""
numero_ingresado = 0
contador = 0
cantidad_ingresada = 0

print('Ingrese un numero: ')
numero_ingresado = int(input())

while numero_ingresado != 0:
    contador = contador + numero_ingresado
    cantidad_ingresada += 1
    print('Ingrese un numero: ')
    numero_ingresado = int(input())

print("La suma es " + str(contador))
print("La media es " + str(contador / cantidad_ingresada))



