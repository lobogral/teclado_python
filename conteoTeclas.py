from os import listdir

# Abro archivo y obtengo texto en minúsculas
archivo = open('quijote.txt', encoding="utf-8")
texto = archivo.read().lower()

# Obtengo la frecuencia de los caracteres
frecCaracteres={}
for caracter in texto:
    if caracter in frecCaracteres:
        frecCaracteres[caracter]+=1
    else:
        frecCaracteres[caracter]=1

# Agrego frecuencias de los caracteres con tilde a los que no tienen tilde
# Agrego frecuencias de la tilde
relAcentosNoAcentos = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u'
}
frecCaracteres['´'] = 0
for caracter in frecCaracteres:
    if caracter in list(relAcentosNoAcentos.keys()): 
        caracterSinAcento = relAcentosNoAcentos[caracter]
        frecCaracteres[caracterSinAcento] += frecCaracteres[caracter]
        frecCaracteres["´"] += frecCaracteres[caracter]

# Agrego frecuencias de los caracteres con dieresis a los que no tienen dieresis
# Agrego frecuencias de la dieresis
frecCaracteres['¨'] = 0
frecCaracteres['u'] += frecCaracteres['ü']
frecCaracteres['¨'] += frecCaracteres['ü']


# Remuevo caracteres que no se utilizarán (Por ahora)
caracteresRetirar =  ['(', ')', '¿', '?', '¡', '!', '»', '«', '[', ']']
caracteresRetirar += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracteresRetirar += ["'", '"', '-', '—', '*', '\n', '\ufeff']
caracteresRetirar += ['á', 'é', 'í', 'ó', 'ú', 'ü']
caracteresRetirar += ['ù', 'à', 'ï']

for caracter in caracteresRetirar:
    frecCaracteres.pop(caracter, None)


# Ordeno los caracteres para una lectura más fácil
frecCaracteres = dict(sorted(frecCaracteres.items(),
                             key=lambda x: x[1],
                             reverse = True))

for caracter, frecuencia in frecCaracteres.items():
    print(repr(caracter) + " : " + str(frecuencia))

# Comprobación texto vs diccionario
print(len(texto))
print(sum([value for key, value in frecCaracteres.items()]))




