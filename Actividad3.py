
class Scrabble():
    # Declaramos un diccionario como constante con las palabra(Key) y sus puntajes(Value).
    DICCIONARIO = {"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":2,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
    puntos = 0

    # Creamos nuestro constructor y pasamos la palabra ingresada por argumento.
    def __init__(self,palabra):
        
        self.palabra = palabra
        ok = True
        while ok:
            # Validamos que el usuario ingrese dos palabras como minimo
            try:
                if len(self.palabra) < 2:
                    while ok:
                        print("Error:\nLa palabra debe estar conformada por almenos dos letras")
                        self.palabra = input("Ingrese una palabra conformada por dos letras:").upper()
                        if len(self.palabra) > 1:
                            ok = False
                    self.analiza_palabra()
                else:
                    self.analiza_palabra()
                    ok = False

            # En caso de que el usuario ingrese algun caracter invalido que no pertenece al diccionario.
            except KeyError:
                print("Error:\nPalabra no encontrada.")
                self.palabra = input("Ingrese una palabra conformada por dos letras:").upper()

    # Analizamos las letras una a una y vamos sumando sus puntos de acuerdo al match con el diccionario.
    def analiza_palabra(self):
        for letra in self.palabra:
            if self.DICCIONARIO[letra]:
                self.puntos += self.DICCIONARIO[letra]
    
    # Mostramos el puntaje obtenido.
    def puntaje(self):
         print("Puntaje obtenido: ",self.puntos)


# Creamos el objeto jugar para ser analizado por nuestro metodo analiza_palabra().
jugar = Scrabble(input("Ingrese una palabra conformada por dos letras:").upper())
jugar.puntaje()



