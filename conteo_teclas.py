# Abro archivo y obtengo texto en minúsculas
with open('quijote.txt', encoding="utf-8") as archivo:
    texto = archivo.read().lower()

# Obtengo la frecuencia de los caracteres
frec_caracteres: dict[str, int] = {}

for caracter in texto:
    if caracter in frec_caracteres:
        frec_caracteres[caracter] += 1
    else:
        frec_caracteres[caracter] = 1

# Agrego frecuencias de los caracteres con tilde a los que no tienen tilde
# Agrego frecuencias de la tilde
rel_acentos_no_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
frec_caracteres['´'] = 0
for acento, no_acento in rel_acentos_no_acentos.items():
    frec_caracteres[no_acento] += frec_caracteres[acento]
    frec_caracteres["´"] += frec_caracteres[acento]

# Agrego frecuencias de los caracteres con dieresis a los que no tienen dieresis
# Agrego frecuencias de la dieresis
frec_caracteres['¨'] = 0
frec_caracteres['u'] += frec_caracteres['ü']
frec_caracteres['¨'] += frec_caracteres['ü']


# Remuevo caracteres que no se utilizarán (Por ahora)
caracteres_retirar = ['(', ')', '¿', '?', '¡', '!', '»', '«', '[', ']']
caracteres_retirar += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteres_retirar += ["'", '"', '-', '—', '*', '\n', '\ufeff']
caracteres_retirar += ['á', 'é', 'í', 'ó', 'ú', 'ü']
caracteres_retirar += ['ù', 'à', 'ï']

for caracter in caracteres_retirar:
    frec_caracteres.pop(caracter, None)


# Ordeno los caracteres para una lectura más fácil
frec_caracteres = dict(sorted(frec_caracteres.items(),
                              key=lambda x: x[1],
                              reverse=True))

for caracter, frecuencia in frec_caracteres.items():
    print(repr(caracter) + " : " + str(frecuencia))

# Comprobación texto vs diccionario
print(len(texto))
print(sum([value for key, value in frec_caracteres.items()]))
