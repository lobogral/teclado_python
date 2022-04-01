import os

nombre_libro = 'LaRegenta'
#nombre_libro = 'DonQuijote'
#nombre_libro = 'ElInternetYLosIdiomas'
#nombre_libro = 'LaRanaViajera'
#nombre_libro = 'LaNinaRobada'

def frecuencia_filas(nom_teclado, caracs_fila_superior, caracs_fila_media):
    frec_fila_superior: int = 0
    frec_fila_media: int = 0
    frec_fila_inferior: int = 0

    for carac, frec in caracs.items():
        if carac in caracs_fila_superior:
            frec_fila_superior += frec
        elif carac in caracs_fila_media:
            frec_fila_media += frec
        else:
            frec_fila_inferior += frec

    texto = ""
    texto += "\n ------------------------------------"
    texto += "\n Teclado " + nom_teclado + ":"
    texto += "\n ------------------------------------"
    texto += "\n Frecuencia fila superior: " + str(frec_fila_superior)
    texto += "\n Frecuencia fila media: " + str(frec_fila_media)
    texto += "\n Frecuencia fila inferior: " + str(frec_fila_inferior)
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
caracs_fila_superior = "qwertyuiop´"
caracs_fila_media = "asdfghjklñ"
texto_archivo += frecuencia_filas("qwerty", caracs_fila_superior, caracs_fila_media)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_fila_superior = ".,ñpyfgchl"
caracs_fila_media = "aoeuidrtns´"
texto_archivo += frecuencia_filas("dvorak", caracs_fila_superior, caracs_fila_media)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_fila_superior = "qwfpgjluyñ´"
caracs_fila_media = "arstdhneio"
texto_archivo += frecuencia_filas("colemak", caracs_fila_superior, caracs_fila_media)

# Creo un archivo de analisis
nombre_carpeta = 'resultados_carga_filas_teclado'
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)

archivo = open(nombre_carpeta + '/analisis' + nombre_libro + '.txt', "w")
archivo.write(texto_archivo)
archivo.close()
