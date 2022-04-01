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


# Obtengo la frecuencia de las combinaciones
frec_combs: dict[str, int] = {}

caracter_inicial = texto[0]
caracter_final = ""
texto = texto[1:]

for caracter_final in texto:
    
    if caracter_inicial + caracter_final in frec_combs:
        frec_combs[caracter_inicial + caracter_final] += 1
    else:
        frec_combs[caracter_inicial + caracter_final] = 1

    caracter_inicial = caracter_final

# Analizo situación de las tildes (Agrego frecuencias a vocales)
rel_signs = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u'
}

copia_frec_combs = frec_combs.copy()

for comb, frec in copia_frec_combs.items():
    if comb[0] in "áéíóú":
        if rel_signs[comb[0]] + comb[1] in frec_combs:
            frec_combs[rel_signs[comb[0]] + comb[1]] += frec
        else:
            frec_combs[rel_signs[comb[0]] + comb[1]] = frec
    if comb[1] in "áéíóú":
        if comb[0] + '´' in frec_combs:
            frec_combs[comb[0] + '´'] += frec
        else:
            frec_combs[comb[0] + '´'] = frec

for caracter in texto:
    if (caracter in "áéíóú"):
        if '´' + rel_signs[caracter] in frec_combs:
            frec_combs['´' + rel_signs[caracter]] += 1
        else:
            frec_combs['´' + rel_signs[caracter]] = 1


# Retiro caracteres que no se van a evaluar
"""
Nota: Se define conmutatividad, es decir:
por ejemplo 'ia' es lo mismo que 'ai', en lo que se refiere a la sobrecarga
"""
combs_utils = string.ascii_lowercase + "ñ,.´"
frec_comb_utils: dict[str, int] = {}

for comb, frec in frec_combs.items():
    if (comb[0] in combs_utils) and (comb[1] in combs_utils) and (comb[0] != comb[1]):
        if (comb[1] + comb[0]) in frec_comb_utils:
            frec_comb_utils[comb[1] + comb[0]] += frec
        else:
            frec_comb_utils[comb] = frec


# Ordeno los caracteres para una lectura más fácil
frec_comb_utils = dict(sorted(frec_comb_utils.items(),
                              key=lambda x: x[1],
                              reverse=True))

# Creo un archivo de analisis
nombre_carpeta = 'resultados_conteo_sobrecarga'
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)
    
archivo = open(nombre_carpeta + '/analisis' + nombre_libro + '.txt', "w")
archivo.write("Combinacion  Frecuencia")
for comb_util, frecuencia in frec_comb_utils.items():
    archivo.write("\n" + comb_util + "           " + str(frecuencia))
archivo.close()
