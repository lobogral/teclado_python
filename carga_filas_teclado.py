nombre_archivo = 'LaRegenta.txt'

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

    print("------------------------------------")
    print("Teclado " + nom_teclado + ":")
    print("------------------------------------")
    print("Frecuencia fila superior: " + str(frec_fila_superior))
    print("Frecuencia fila media: " + str(frec_fila_media))
    print("Frecuencia fila inferior: " + str(frec_fila_inferior))

# Abro archivo y obtengo diccionario
with open('resultados_conteo_carga/analisis' + nombre_archivo) as archivo:
    archivo.readline()
    texto = archivo.read()

caracs = dict(linea.split() for linea in texto.split("\n"))
caracs = dict((carac, int(frec)) for carac, frec in caracs.items())

# Distribucion de toda la vida
caracs_fila_superior = "qwertyuiop´"
caracs_fila_media = "asdfghjklñ"
frecuencia_filas("qwerty", caracs_fila_superior, caracs_fila_media)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_fila_superior = ".,ñpyfgchl"
caracs_fila_media = "aoeuidrtns´"
frecuencia_filas("dvorak", caracs_fila_superior, caracs_fila_media)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_fila_superior = "qwfpgjluyñ´"
caracs_fila_media = "arstdhneio"
frecuencia_filas("colemak", caracs_fila_superior, caracs_fila_media)
