
nucleo_familiar = {
    "12345678A": "Josefa",
    "98765432B": "Mario",
    "56789012C": "Marcela",
    "34567890D": "Violeta",
    "87654321E": "Carolina",
    "43210987F": "Sebastian"
}

# Imprimir el diccionario del núcleo familiar
for dni, nombre in nucleo_familiar.items():
    print(f"DNI: {dni}, Nombre: {nombre}")

nucleo_familiar = {
    "12345678A": "Josefa",
    "98765432B": "Mario",
    "56789012C": "Marcela",
    "34567890D": "Violeta",
    "87654321E": "Carolina",
    "43210987F": "Sebastian"
}

familia_ampliada = {
    "12548551X": "Abuelo Paterno_Juan",
    "52548795Y": "Abuela Paterna_Miriam",
    "31487555Z": "Abuelo Materno_Jose",
    "11458721W": "Abuela Materna_Maria",
    "25248565V": "Cuñado_jose",
    "26147856U": "Cuñada_Natalia"
}

# Combinar los diccionarios de núcleo familiar y familia ampliada
diccionario_completo = {**nucleo_familiar, **familia_ampliada}

# Imprimir el diccionario completo
for dni, nombre in diccionario_completo.items():
    print(f"DNI: {dni}, Nombre: {nombre}")
