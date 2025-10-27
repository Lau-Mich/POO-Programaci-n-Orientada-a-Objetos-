#EJEMPLO DE INSTRUCTOR
#definir una clase
class estudiantes:
     def __init__(self, nombre, edad, programa_formacion):
         self.nombre=nombre
         self.edad=edad
         self.programa_formacion=programa_formacion

     def mostrar_informacion(self):
         print(f"nombre: {self.nombre}")
         print(f"edad: {self.edad}")
         print(f"self.programa_formacion: {self.programa_formacion}")

#creacion de una instancia del objeto

est1=estudiantes("laura gomez" , 20 , "programacion de software")
est2=estudiantes("clara perez", 24, "programacion de software")

#mostrar informacion
est1.mostrar_informacion()
est2.mostrar_informacion()

#EJERCICIOS
print("\n-----mini-proyecto-----")
print("AGENDA DE CONTACTOS")
class Contactos:
    def __init__(self, nombre, apellido, numero):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero

    def mostrar_contactos(self):
        print("-----------------------")
        print(f"nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"numero: {self.numero}")

contacto1=Contactos("Lauren", "Gutierrez", 3022072618)
contacto2=Contactos("Valery", "Rincon", 3177068832)
contacto3=Contactos("Luis", "Riveros", 3052388937)

contacto1.mostrar_contactos()
contacto2.mostrar_contactos()
contacto3.mostrar_contactos()


print("------------------------------------------------------")
print("SISTEMA DE VOTACION\n")

class Candidato:
    def __init__(self, nombre):
        self.nombre=nombre
        self.votos= 0

    def votar(self):
        self.votos=self.votos + 1

    def mostrar(self):
        print(f"Candidato: {self.nombre} - Votos: {self.votos}")

candidato1 = Candidato("Ana")
candidato2 = Candidato("Luis")

candidato1.votar()
candidato1.votar()
candidato2.votar()

candidato1.mostrar()
candidato2.mostrar()


print("------------------------------------------------")
print("GESTOR DE PRODUCTOS\n")

class Producto:
    def __init__(self, nombre, precio): 
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

producto1 = Producto("Manzana", 2.5)
producto2 = Producto("Pan", 1.0)
producto3 = Producto("Leche", 3.0)

print("---------")
producto1.mostrar()
producto2.mostrar()
producto3.mostrar()
 