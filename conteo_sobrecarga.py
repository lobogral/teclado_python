import string
import os

nombre_archivo = 'LaRegenta.txt'

# Abro archivo y obtengo texto en minúsculas
with open(nombre_archivo, encoding="utf-8") as archivo:
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

# Analizo situación de las tildes y la diéresis (Agrego frecuencias a vocales)
"""
Nota: Solo se analiza un caso
aá -> a´a
áa -> ´aa
áá -> ´a´a
El caso 2 se analiza por continuidad
"""

rel_signs = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u'
}

copia_frec_combs = frec_combs.copy()

for comb, frec in copia_frec_combs.items():
    if (comb[0] in "áéíóúü") and (comb[1] not in "áéíóúü"):
        if rel_signs[comb[0]] + comb[1] in frec_combs:
            frec_combs[rel_signs[comb[0]] + comb[1]] += frec
        else:
            frec_combs[rel_signs[comb[0]] + comb[1]] = frec


# Retiro caracteres que no se van a evaluar
"""
Nota: Se define conmutatividad, es decir:
por ejemplo 'ia' es lo mismo que 'ai', en lo que se refiere a la sobrecarga
"""
combs_utils = string.ascii_lowercase + "ñ"
frec_comb_utils: dict[str, int] = {}

for comb, frec in frec_combs.items():
    if (comb[0] in combs_utils) and (comb[1] in combs_utils):
        if (comb[1] + comb[0]) in frec_comb_utils:
            frec_comb_utils[comb[1] + comb[0]] += frec
        else:
            frec_comb_utils[comb] = frec


# Ordeno los caracteres para una lectura más fácil
frec_comb_utils = dict(sorted(frec_comb_utils.items(),
                              key=lambda x: x[1],
                              reverse=True))

# Creo un archivo de analisis
if not os.path.exists('resultados_conteo_sobrecarga'):
    os.mkdir('resultados_conteo_sobrecarga')
    
archivo = open('resultados_conteo_sobrecarga/analisis' + nombre_archivo, "w")
for comb_util, frecuencia in frec_comb_utils.items():
    archivo.write(repr(comb_util) + " : " + str(frecuencia) + "\n")
archivo.close()
