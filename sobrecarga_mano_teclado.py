nombre_archivo = 'LaRegenta.txt'

def conteo_sobrecarga(nom_teclado, caracs_izquierda):
    sobrecarga: int = 0
    no_sobrecarga: int = 0

    for comb, frec in frec_combs.items():
        if (comb[0] in caracs_izquierda) and (comb[1] not in caracs_izquierda):
            sobrecarga += frec
        elif (comb[0] not in caracs_izquierda) and (comb[1] in caracs_izquierda):
            sobrecarga += frec
        else:
            no_sobrecarga += frec

    print("------------------------------------")
    print("Teclado " + nom_teclado + ":")
    print("------------------------------------")
    print("Frecuencia sobrecarga: " + str(sobrecarga))
    print("Frecuencia no sobrecarga: " + str(no_sobrecarga))

# Abro archivo y obtengo diccionario
with open('resultados_conteo_sobrecarga/analisis' + nombre_archivo) as archivo:
    archivo.readline()
    texto = archivo.read()

frec_combs = dict(linea.split() for linea in texto.split("\n"))
frec_combs = dict((comb, int(frec)) for comb, frec in frec_combs.items())


# Distribucion de toda la vida
caracs_izquierda = "qwertasdfgzxcvb"
conteo_sobrecarga("qwerty", caracs_izquierda)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_izquierda = ".,ñpyaoeuiqjk"
conteo_sobrecarga("dvorak", caracs_izquierda)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_izquierda = "qwfpgarstdzxcvb"
conteo_sobrecarga("colemak", caracs_izquierda)
