import string
import os

nombre_libro = 'LaRegenta'
#nombre_libro = 'DonQuijote'
#nombre_libro = 'ElInternetYLosIdiomas'
#nombre_libro = 'LaRanaViajera'
#nombre_libro = 'LaNinaRobada'

# Abro archivo y obtengo texto en minúsculas
with open(nombre_libro + '.txt', encoding="utf-8") as archivo:
    texto = archivo.read().lower()

# Obtengo la frecuencia de los caracteres
frec_caracs: dict[str, int] = {}

for caracter in texto:
    if caracter in frec_caracs:
        frec_caracs[caracter] += 1
    else:
        frec_caracs[caracter] = 1

# Analizo situación de las tildes
"""
Nota: Agrego frecuencias a las vocales
y agrego frecuencias a las tildes

Nota: La dieresis no se analiza porque
es despreciable
"""
frec_caracs['´'] = 0
rel_signs = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u'
}

for sign, no_sign in rel_signs.items():
    frec_caracs[no_sign] += frec_caracs[sign]
    frec_caracs['´'] += frec_caracs[sign]

# Creo diccionario con las frecuencias de la letras
caracs_utils = string.ascii_lowercase + "ñ´,."
frec_caracs_utils: dict[str, int] = {}

for carac_util in caracs_utils:
    if carac_util in frec_caracs:
        frec_caracs_utils[carac_util] = frec_caracs[carac_util]
    else:
        frec_caracs_utils[carac_util] = 0


# Ordeno los caracteres para una lectura más fácil
frec_caracs_utils = dict(sorted(frec_caracs_utils.items(),
                                key=lambda x: x[1],
                                reverse=True))

# Creo un archivo de analisis
nombre_carpeta = 'resultados_conteo_carga'
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)

archivo = open(nombre_carpeta + '/analisis' + nombre_libro + '.txt', "w")
archivo.write("Caracter  Frecuencia")
for carac_util, frecuencia in frec_caracs_utils.items():
    archivo.write("\n" + carac_util + "         " + str(frecuencia))
archivo.close()
