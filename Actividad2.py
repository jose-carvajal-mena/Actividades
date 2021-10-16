class AlmacenaPalabras():

    # Lista que guardara nuetras palabras.
    lista_palabras = []

    # Creamos nuestro constructor y recibimos el parametro "palabra".
    def __init__(self,palabra):
        self.lista_palabras.append(palabra)
        self.lista_palabras

    # Metodo para realizar la limpieza de los datos repetidos.
    def gurda_palabras(self):

        self.lista_no_repetidas = []

        for i in self.lista_palabras:

            # Indicamos a la lista que si el valor no esta agregarlo.
            if i not in self.lista_no_repetidas:
                self.lista_no_repetidas.append(i)

        return self.lista_no_repetidas


# Creamos un flag para manejar la entrada por teclado.
Ok = True
palabra = ""
while Ok:

    palabra = input("Ingrese palabra: ")
    if palabra != "***":
        # Creamos nuestro objeto y pasamos las palabras a nuestro constructor.
        datos = AlmacenaPalabras(palabra)
        Ok = True
    else:
        Ok = False

print(datos.gurda_palabras())

