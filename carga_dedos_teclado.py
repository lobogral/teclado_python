nombre_archivo = 'LaRegenta.txt'

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

    print("------------------------------------")
    print("Teclado " + nom_teclado + ":")
    print("------------------------------------")
    print("Frecuencia facil: " + str(frec_facil))
    print("Frecuencia intermedia: " + str(frec_intermedio))
    print("Frecuencia dificil: " + str(frec_dificil))

# Abro archivo y obtengo diccionario
with open('resultados_conteo_carga/analisis' + nombre_archivo) as archivo:
    archivo.readline()
    texto = archivo.read()

caracs = dict(linea.split() for linea in texto.split("\n"))
caracs = dict((carac, int(frec)) for carac, frec in caracs.items())

# Distribucion de toda la vida
caracs_facil = "asdfjklñei"
caracs_intermedio = "wruoghcvnm"
frecuencia_dedos("qwerty", caracs_facil, caracs_intermedio)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_facil = "aoeurtnsñc"
caracs_intermedio = ",pghidqjbm"
frecuencia_dedos("dvorak", caracs_facil, caracs_intermedio)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_facil = "arstneiofu"
caracs_intermedio = "wplydhcvm,"
frecuencia_dedos("colemak", caracs_facil, caracs_intermedio)
