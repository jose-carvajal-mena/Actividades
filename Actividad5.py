
class SumaNumeros():
    # Variables para controlar nuestros datos.
    numero = 0
    acumulador = 0
    
    # constructor de nustra clase, aqui realizamos toda la logica de sumatoria.
    def __init__(self):
        # Iniciamos un bucle para controlar la ejecucion de nuestro programa.
         while True:
             # con try except controlamos errores de entrada y salida.
            try:
                self.acumulador = input("Ingrese numero:")
                if self.acumulador == " ":
                    break
                else:
                    self.numero += int(self.acumulador)
                    print("Resultado de la suma: ",self.numero)
            except ValueError:
                print("ERROR:\nCaracter invalido")
            

    # Metodo para mostrar mensaje de salida
    def mensaje_saida(self):
        print("Ha abandonado el programa.")

# Creamos nuestro objeto "numeros", y hacemos la llamada al metodo "mensaje_salida()".
numeros = SumaNumeros()
numeros.mensaje_saida()

