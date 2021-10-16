# Modulo para la utilizacion de la lectura de teclas.
import msvcrt

# Creamos la clase para la manipulacion de los numeros.
class NumerosOrdenados():

    # Inicializamos una lista vacia para ir almacenando los numeros ingresados por el usuario.
    lista_numeros = []

    # Este metodo nos sirve para controlar y validar la cantidad de numeros a leer.
    def cantidad_numeros(self):
        print("Ingrese un numero entre 2 y 20 con los numeros de su teclado y presione la tecla [enter]: ")
        ok = True
        while ok:
            try:
                numero = int(input())
                if numero >= 2 and numero <= 20:
                    self.guarda_numeros(numero)
                    ok = False
                else:
                   self.mensajes_errores(3)
            except ValueError:
                self.mensajes_errores(2)

    # Metodo para ir guardando los numeros que ingresa el usuario en un la lista_numeros.
    def guarda_numeros(self,cantidad_numeros):
        
            print("Comienze a ingresar su numeros por favor:")
            numeros_ingresados = 0
            while cantidad_numeros > numeros_ingresados:
                
                # Parceamos a entero el codigo de la tecla leida con getwch().
                numero = int(msvcrt.getwch())
                
                if numero != 0:
                    print("Ha ingresado el numero  [%s] "%(str(numero)),"a la lista.")
                    self.lista_numeros.append(numero)
                    numeros_ingresados += 1
                else:
                    print("Ha salido del programa.")
                    self.lista_numeros.sort(reverse=False)
                    print("Sus numeros fueron %s"%(self.lista_numeros),"y fueron ordenados ascendentemente por defecto.")
                    exit()
            
    
    # Metodo para ordenar los numeros de manera Ascendente o Descendente , mediante el parametro orden.
    def ordenar_numeros(self,orden):
        if orden.upper() == 'A':
            self.lista_numeros.sort(reverse=False)
            print(self.lista_numeros)
        elif orden.upper() == 'D':
            self.lista_numeros.sort(reverse=True)
            print(self.lista_numeros)
        else:
            self.mensajes_errores(1)

    # Metodo para tratar errores en los distintos metodos.
    def mensajes_errores(self,error):

        if error == 1:
            orden = input("ERROR:\nPor favor seleccione una opcion valida, A(Ascendente) ó D(Descendente):")
            self.ordenar_numeros(orden)
        elif error == 2:
              print("ERROR:\nDeber ingresar un numero entre 2 y 20 con los numeros de su teclado y presione la tecla [enter]:  ")
              ok =  True
        elif error == 3:
             print("ADVERTENCIA:\nLa cantidad ingresada exede el maximo o el minimo del numero a ingresar.")
             print("Deber ingresar un numero entre 2 y 20 con los numeros de su teclado y presione la tecla [enter]:  ")
             ok = True
        else:
            print("Error desconocido.")

# Creamos nuestro objeto.
numeros = NumerosOrdenados()

# y utilizamos nuestros metodos.
numeros.cantidad_numeros()
orden = input("¿Como desea ordenar los numeros A(Ascendente) ó D(Descendente)?: ")
# Se realiza para demostrar el trabajo con parametros.
numeros.ordenar_numeros(orden)