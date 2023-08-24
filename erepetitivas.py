# Parte 1: Verificar si el número es igual a 10 y dar mensajes según su valor
print("Ingrese un número:")
num = int(input())

if num == 10:
    print("¡Usted ha ganado el sorteo!")
else:
    if num < 10:
        print("¡Falto un poco, sigue participando!")
    else:
        print("¡Te pasaste, a seguir intentando!")

# Parte 2: Verificar el día de la semana ingresado
print("Ingrese un día de la semana:")
dia = input()

if dia.lower() == "lunes":
    print("Es inicio de semana, ánimo.")
elif dia.lower() == "viernes":
    print("¡Viernes, el fin de semana está cerca!")
elif dia.lower() == "sábado" or dia.lower() == "domingo":
    print("¡Es fin de semana, a disfrutar!")
else:
    print("No reconocí ese día, ¿seguro que lo escribiste bien?")

# Parte 3: Verificar si una letra es vocal
print("Ingrese una letra:")
letra = input().lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Es vocal.")
else:
    print("No es vocal.")
