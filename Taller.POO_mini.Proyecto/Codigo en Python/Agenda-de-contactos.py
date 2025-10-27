#agenda de contactos
# la mini agenda mostrara los contactos (apenas 3 JAJA) que tiene como informacion:
# nombre, telefono y email.

# 12. implementa en python las clases de tu diagrama
# la clase base es contacto, que basicamente guarda lo mas basico:
# nombre, telefono y email.

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"telefono: {self.telefono}")
        print(f"email: {self.email}")


# luego aqui va la clase derivada contactoamigo
# 13. agrega atributos, metodos y relacion de herencia

class ContactoAmigo(Contacto):
    def __init__(self, nombre, telefono, email, cumpleaños):
        # super llama al constructor de la clase papa (contacto)
        # para no tener que escribir otra vez lo del nombre, telefono y email.
        super().__init__(nombre, telefono, email)
        self.cumpleaños = cumpleaños  # atributo nuevo solo de los amigos

    # sobrescribi el metodo mostrar_info (polimorfismo)
    def mostrar_info(self):
        super().mostrar_info()  # primero muestra los datos normales
        print(f"cumpleaños: {self.cumpleaños}")  # luego lo especial del amigo, que ps  en este caso es la fecha de cumple


# y aqui clase derivada contactotrabajo

class ContactoTrabajo(Contacto):
    def __init__(self, nombre, telefono, email, empresa):
        super().__init__(nombre, telefono, email)
        self.empresa = empresa  # atributo nuevo solo del trabajo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"empresa: {self.empresa}")


# ---------------------------------------------------------------
# o sea: contactoamigo y contactotrabajo heredan de contacto
# esto significa que automaticamente tienen nombre, telefono y email
# sin tener que escribirlo otra vez. solo agregan lo que los hace distintos:
# contactoamigo → cumpleaños
# contactotrabajo → empresa
# pd: me embollé un poco en la herencia pero ya lo corregi jaja no te preocupes mayron.
# ---------------------------------------------------------------


# 14. ejemplo de polimorfismo
# aqui se demuestra el polimorfismo porque aunque todas las variables
# son tipo contacto, cada una se comporta diferente al ejecutar mostrar_info.
# cada clase imprime cosas distintas

# cree los contactos ya predefinidos, apenas 3 jaja
contacto1 = Contacto("valery rincon", 310-123-4567, "valery@email.com")   # valery como contacto normal
contacto2 = ContactoAmigo("luis riveros", 320-987-6543, "luis@email.com", "15/07")  # luis como contacto amigo
contacto3 = ContactoTrabajo("paulo gutierrez", 315-555-7890, "paulo@trabajo.com", "diamante.sas")  # paulo como contacto de trabajo


# 15. ejecucion del programa y salida
print("=== agenda de contactos ===")
contacto1.mostrar_info() 
print("-------------------------")
contacto2.mostrar_info()  
print("-------------------------")
contacto3.mostrar_info() 
print("-------------------------")
