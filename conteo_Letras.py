import string

nombre_archivo = 'LaRegenta.txt'

# Abro archivo y obtengo texto en minúsculas
with open(nombre_archivo, encoding="utf-8") as archivo:
    texto = archivo.read().lower()

# Obtengo la frecuencia de los caracteres
frec_caracteres: dict[str, int] = {}

for caracter in texto:
    if caracter in frec_caracteres:
        frec_caracteres[caracter] += 1
    else:
        frec_caracteres[caracter] = 1

# Agrego frecuencias de los caracteres con tilde a los que no tienen tilde
rel_acentos_no_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
for acento, no_acento in rel_acentos_no_acentos.items():
    frec_caracteres[no_acento] += frec_caracteres[acento]


# Agrego frecuencias de los caracteres con dieresis a los que no tienen dieresis
frec_caracteres['u'] += frec_caracteres['ü']


# Creo diccionario con las frecuencias de la letras
letras = string.ascii_lowercase + "ñ"
frec_letras: dict[str, int] = {}

for letra in letras:
    if letra in frec_caracteres:
        frec_letras[letra] = frec_caracteres[letra]
    else:
        frec_letras[letra] = 0


# Ordeno los caracteres para una lectura más fácil
frec_letras = dict(sorted(frec_letras.items(),
                          key=lambda x: x[1],
                          reverse=True))

# Creo un archivo de analisis
archivo = open('analisis' + nombre_archivo, "w")
for letra, frecuencia in frec_letras.items():
    archivo.write(repr(letra) + " : " + str(frecuencia) + "\n")
archivo.close()
