import os

nombre_libro = 'LaRegenta'

def conteo_sobrecarga(nom_teclado, caracs_izquierda):
    sobrecarga: int = 0
    no_sobrecarga: int = 0

    for comb, frec in frec_combs.items():
        if (comb[0] in caracs_izquierda) and (comb[1] in caracs_izquierda):
            sobrecarga += frec
        elif (comb[0] not in caracs_izquierda) and (comb[1] not in caracs_izquierda):
            sobrecarga += frec
        else:
            no_sobrecarga += frec

    texto = ""
    texto += "------------------------------------" + "\n"
    texto += "Teclado " + nom_teclado + ":" + "\n"
    texto += "------------------------------------" + "\n"
    texto += "Frecuencia sobrecarga: " + str(sobrecarga) + "\n"
    texto += "Frecuencia no sobrecarga: " + str(no_sobrecarga)
    return texto

# Abro archivo y obtengo diccionario

nombre_carpeta = 'resultados_conteo_sobrecarga' 
with open(nombre_carpeta + '/analisis' + nombre_libro + '.txt') as archivo:
    archivo.readline()
    texto = archivo.read()

frec_combs = dict(linea.split() for linea in texto.split("\n"))
frec_combs = dict((comb, int(frec)) for comb, frec in frec_combs.items())


texto_archivo = ""

# Distribucion de toda la vida
caracs_izquierda = "qwertasdfgzxcvb"
texto_archivo += conteo_sobrecarga("qwerty", caracs_izquierda)

# Distribucion dvorak diseñada para español, fuente:
# jellby.altervista.org/dvorak/index.php
caracs_izquierda = ".,ñpyaoeuiqjkx"
texto_archivo += conteo_sobrecarga("dvorak", caracs_izquierda)

# Distribucion colemak diseñada para español, fuente:
# forum.colemak.com/topic/2519-colemak-para-espanol-latino-win-colemak-for-spanish-la-win/
caracs_izquierda = "qwfpgarstdzxcvb"
texto_archivo += conteo_sobrecarga("colemak", caracs_izquierda)

# Creo un archivo de analisis
nombre_carpeta = 'resultados_sobrecarga_mano_teclado'
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)

archivo = open(nombre_carpeta + '/analisis' + nombre_libro + '.txt', "w")
archivo.write(texto_archivo)
archivo.close()
