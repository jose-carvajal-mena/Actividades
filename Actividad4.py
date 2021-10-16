
class Anagrama():
    # Creamos una lista para almacenar las palabras
    palabras = []

    def __init__(self):
        self.guarda_palabras()

    # Guardamos las palabras ingresadas por el usuario a nuestra listra de palabras.
    def guarda_palabras(self):

        # Contador de palabras ingresadas.
        cantidad_palabra = 0

        # Logica para que el usuario agregue solo 2 palabras.
        while cantidad_palabra < 2:
            # Convertimos nuestra palabra en una lista.
            lista= list(input("ingrese palabra"))

            # Ordenamos nuestras letras de la A a Z.
            lista.sort(reverse=False)

            # Convertimos nuestra palabra en un string(juntamos nuestros caracteres).
            palabra_anagrama = "".join(lista)
            self.palabras.append(palabra_anagrama)
            cantidad_palabra +=1

    # Analizamos si estas palabras son anagramas.
    def analiza_anagrama(self):
        if self.palabras[0] == self.palabras[1]:
            print(f"{self.palabras[0]} y {self.palabras[0]} son anagramas")
        else:
            print(f"{self.palabras[0]} y {self.palabras[0]} no son anagramas")
        



# Creamos nuestra objeto de anagrama.
anagrama = Anagrama()
anagrama.analiza_anagrama()