
    
print("ingrese un numero")
num=int(input())
if num == 10:
   print("¡Usted ha ganado el sorteo!")
if num < 10:
    print("¡Falto un poco,seguí participando!")
if num > 10:
       print("¡Te pasaste, a seguir intentando!")




print("Ingrese un día de la semana:")
dia = input()

if dia == "lunes":
    print("La mente lo sabe, el cuerpo no")
elif dia == "viernes":
    print("El cuerpo lo sabe, la mente se relaja")
elif dia == "sabado" or dia == "domingo":
    print("De relax y sol")
else:
    print("No reconocí ese día, ¿seguro que lo escribiste bien?")




print("Ingrese una vocal")
vocal = input()

if vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U" or vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print("Es una vocal")
else:
    print("No es una vocal")

print("ingresar numero")