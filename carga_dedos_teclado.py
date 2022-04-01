import os

nombre_libro = 'LaRegenta'
#nombre_libro = 'DonQuijote'
#nombre_libro = 'ElInternetYLosIdiomas'
#nombre_libro = 'LaRanaViajera'
#nombre_libro = 'LaNinaRobada'

def frecuencia_dedos(nom_teclado, caracs_facil, caracs_intermedio):
    frec_facil: int = 0
    frec_intermedio: int = 0
    frec_dificil: int = 0

    for carac, frec in caracs.items():
        if carac in caracs_facil:
            frec_facil += frec
        elif carac in caracs_intermedio:
            frec_intermedio += frec
        else:
            frec_dificil += frec

    texto = ""
    texto += "\n ------------------------------------"
    texto += "\n Teclado " + nom_teclado + ":"
    texto += "\n ------------------------------------"
    texto += "\n Frecuencia facil: " + str(frec_facil)
    texto += "\n Frecuencia intermedia: " + str(frec_intermedio)
    texto += "\n Frecuencia dificil: " + str(frec_dificil)
    return texto

# Abro archivo y obtengo diccionario
nombre_carpeta = 'resultados_conteo_carga'
with open(nombre_carpeta + '/analisis' + nombre_libro + '.txt') as archivo:
    archivo.readline()
    texto = archivo.read()

caracs = dict(linea.split() for linea in texto.split("\n"))
caracs = dict((carac, int(frec)) for carac, frec in caracs.items())


texto_archivo = ""

# Distribucion de toda la vida
caracs_facil = "asdfjklñei"
caracs_intermedio = "wruoghcvnm"
texto_archivo += frecuencia_dedos("qwerty", caracs_facil, caracs_intermedio)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_facil = "aoeurtnsñc"
caracs_intermedio = ",pghidqjbm"
texto_archivo += frecuencia_dedos("dvorak", caracs_facil, caracs_intermedio)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_facil = "arstneiofu"
caracs_intermedio = "wplydhcvm,"
texto_archivo += frecuencia_dedos("colemak", caracs_facil, caracs_intermedio)

# Creo un archivo de analisis
nombre_carpeta = 'resultados_carga_dedos_teclado'
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)

archivo = open(nombre_carpeta + '/analisis' + nombre_libro + '.txt', "w")
archivo.write(texto_archivo)
archivo.close()
