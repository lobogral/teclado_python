import string
import os

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

# Analizo situación de las tildes y la diéresis (Agrego frecuencias a vocales)
rel_signs = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u'
}

for sign, no_sign in rel_signs.items():
    frec_caracteres[no_sign] += frec_caracteres[sign]

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

if not os.path.exists('resultados_conteo_carga'):
    os.mkdir('resultados_conteo_carga')

archivo = open('resultados_conteo_carga/analisis' + nombre_archivo, "w")
for letra, frecuencia in frec_letras.items():
    archivo.write(repr(letra) + " : " + str(frecuencia) + "\n")
archivo.close()
